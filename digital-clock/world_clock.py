"""
World Digital Clock - Multiple Time Zones
Python implementation with display options
"""

from datetime import datetime
import pytz
from typing import List, Dict, Optional
import time


class WorldClock:
    """Display current time across multiple time zones"""

    TIMEZONES = {
        'UTC': 'UTC',
        'EST': 'America/New_York',
        'CST': 'America/Chicago',
        'MST': 'America/Denver',
        'PST': 'America/Los_Angeles',
        'GMT': 'Europe/London',
        'CET': 'Europe/Paris',
        'IST': 'Asia/Kolkata',
        'JST': 'Asia/Tokyo',
        'AEST': 'Australia/Sydney',
        'NZST': 'Pacific/Auckland',
        'SGT': 'Asia/Singapore',
        'HKT': 'Asia/Hong_Kong',
        'GST': 'Asia/Dubai',
        'BRT': 'America/Sao_Paulo',
        'SAST': 'Africa/Johannesburg',
        'MSK': 'Europe/Moscow',
        'AKST': 'America/Anchorage',
        'HST': 'Pacific/Honolulu',
    }

    def __init__(self, selected_zones: Optional[List[str]] = None):
        """
        Initialize WorldClock
        
        Args:
            selected_zones: List of timezone names to display
        """
        self.selected_zones = selected_zones or ['UTC', 'America/New_York', 'Asia/Tokyo']
        self.time_format = '24'  # '24' or '12'

    def get_time_in_timezone(self, tz_name: str) -> datetime:
        """
        Get current time in specified timezone
        
        Args:
            tz_name: Timezone name (e.g., 'America/New_York')
        
        Returns:
            datetime object in that timezone
        """
        try:
            tz = pytz.timezone(tz_name)
            return datetime.now(tz)
        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Unknown timezone: {tz_name}")
            return datetime.now(pytz.UTC)

    def format_time(self, dt: datetime, format_type: str = '24') -> str:
        """
        Format time as string
        
        Args:
            dt: datetime object
            format_type: '24' for 24-hour or '12' for 12-hour format
        
        Returns:
            Formatted time string
        """
        if format_type == '24':
            return dt.strftime('%H:%M:%S')
        else:
            return dt.strftime('%I:%M:%S %p')

    def format_date(self, dt: datetime) -> str:
        """
        Format date as string
        
        Args:
            dt: datetime object
        
        Returns:
            Formatted date string (e.g., 'Mon Jan 15')
        """
        return dt.strftime('%a %b %d')

    def get_timezone_offset(self, tz_name: str) -> str:
        """
        Get UTC offset for timezone
        
        Args:
            tz_name: Timezone name
        
        Returns:
            UTC offset string (e.g., '+05:30')
        """
        try:
            dt = self.get_time_in_timezone(tz_name)
            offset = dt.strftime('%z')
            return f"{offset[:3]}:{offset[3:]}"
        except Exception as e:
            return "N/A"

    def get_timezone_info(self, tz_name: str) -> Dict:
        """
        Get timezone information
        
        Args:
            tz_name: Timezone name
        
        Returns:
            Dictionary with timezone info
        """
        # Find short name from TIMEZONES dict
        short_name = None
        for short, long_name in self.TIMEZONES.items():
            if long_name == tz_name:
                short_name = short
                break
        
        return {
            'short_name': short_name or tz_name.split('/')[-1],
            'full_name': tz_name,
            'offset': self.get_timezone_offset(tz_name)
        }

    def add_timezone(self, tz_name: str) -> None:
        """
        Add timezone to display list
        
        Args:
            tz_name: Timezone name to add
        """
        if tz_name not in self.selected_zones:
            self.selected_zones.append(tz_name)

    def remove_timezone(self, tz_name: str) -> None:
        """
        Remove timezone from display list
        
        Args:
            tz_name: Timezone name to remove
        """
        if tz_name in self.selected_zones:
            self.selected_zones.remove(tz_name)

    def get_all_times(self) -> Dict[str, str]:
        """
        Get current time in all selected timezones
        
        Returns:
            Dictionary with timezone as key and formatted time as value
        """
        times = {}
        for tz in self.selected_zones:
            dt = self.get_time_in_timezone(tz)
            times[tz] = self.format_time(dt, self.time_format)
        return times

    def display_simple(self) -> None:
        """Display times in simple text format"""
        print("\n" + "="*60)
        print("🌍 WORLD CLOCK - CURRENT TIME IN ALL TIMEZONES")
        print("="*60 + "\n")

        for tz in self.selected_zones:
            dt = self.get_time_in_timezone(tz)
            info = self.get_timezone_info(tz)
            
            print(f"📍 {info['short_name']:6} | {info['full_name']:25} | {self.format_time(dt, self.time_format)}")
            print(f"   UTC {info['offset']:6} | {self.format_date(dt)}")
            print()

    def display_table(self) -> None:
        """Display times in table format"""
        print("\n" + "┌" + "─"*70 + "┐")
        print("│ 🌍 WORLD CLOCK - CURRENT TIME IN ALL TIMEZONES" + " "*23 + "│")
        print("├" + "─"*70 + "┤")

        # Header
        print("│ {:8} │ {:25} │ {:15} │ {:10} │".format(
            "Abbrev", "Timezone", "Time", "UTC Offset"
        ))
        print("├" + "─"*70 + "┤")

        # Data rows
        for tz in self.selected_zones:
            dt = self.get_time_in_timezone(tz)
            info = self.get_timezone_info(tz)
            
            print("│ {:8} │ {:25} │ {:15} │ {:10} │".format(
                info['short_name'],
                info['full_name'][:25],
                self.format_time(dt, self.time_format),
                info['offset']
            ))

        print("└" + "─"*70 + "┘\n")

    def display_compact(self) -> None:
        """Display in compact single-line format"""
        times = self.get_all_times()
        print("\n🌍 World Clock: ", end="")
        print(" | ".join([f"{tz.split('/')[-1]}: {time}" for tz, time in times.items()]))

    def live_display(self, format_type: str = 'table', interval: int = 1) -> None:
        """
        Display live updating clock
        
        Args:
            format_type: 'simple', 'table', or 'compact'
            interval: Update interval in seconds
        """
        self.time_format = '24'
        
        try:
            while True:
                # Clear screen (platform-independent)
                import os
                os.system('cls' if os.name == 'nt' else 'clear')

                if format_type == 'table':
                    self.display_table()
                elif format_type == 'simple':
                    self.display_simple()
                else:
                    self.display_compact()

                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n👋 Clock stopped")

    def export_to_dict(self) -> Dict:
        """
        Export current times as dictionary
        
        Returns:
            Dictionary with timezone info and current times
        """
        return {
            tz: {
                'time': self.format_time(self.get_time_in_timezone(tz), self.time_format),
                'date': self.format_date(self.get_time_in_timezone(tz)),
                'offset': self.get_timezone_offset(tz),
                'info': self.get_timezone_info(tz)
            }
            for tz in self.selected_zones
        }


# ==================== USAGE EXAMPLES ====================

def example_1_simple_display():
    """Example 1: Simple display"""
    print("\n📌 Example 1: Simple Display\n")
    clock = WorldClock(['UTC', 'America/New_York', 'Asia/Tokyo'])
    clock.display_simple()


def example_2_table_display():
    """Example 2: Table display"""
    print("\n📌 Example 2: Table Display\n")
    clock = WorldClock(['UTC', 'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney'])
    clock.display_table()


def example_3_get_times():
    """Example 3: Get times programmatically"""
    print("\n📌 Example 3: Get Times Programmatically\n")
    clock = WorldClock(['UTC', 'America/New_York', 'Asia/Tokyo'])
    times = clock.get_all_times()
    
    for tz, time_str in times.items():
        print(f"{tz}: {time_str}")


def example_4_custom_timezones():
    """Example 4: Custom timezone selection"""
    print("\n📌 Example 4: Custom Timezones\n")
    clock = WorldClock()
    clock.selected_zones = ['America/New_York', 'Europe/Paris', 'Asia/Dubai', 'Australia/Sydney']
    clock.display_table()


def example_5_add_remove_timezones():
    """Example 5: Dynamically add/remove timezones"""
    print("\n📌 Example 5: Add/Remove Timezones\n")
    clock = WorldClock(['UTC', 'America/New_York'])
    
    print("Initial timezones:")
    clock.display_simple()
    
    print("Adding Asia/Tokyo and Europe/London...")
    clock.add_timezone('Asia/Tokyo')
    clock.add_timezone('Europe/London')
    clock.display_simple()


def example_6_live_clock():
    """Example 6: Live updating clock (uncomment to use)"""
    print("\n📌 Example 6: Live Clock (Press Ctrl+C to stop)\n")
    clock = WorldClock(['UTC', 'America/New_York', 'Asia/Tokyo'])
    # Uncomment to run live display:
    # clock.live_display(format_type='table', interval=1)


def example_7_export_data():
    """Example 7: Export data"""
    print("\n📌 Example 7: Export to Dictionary\n")
    clock = WorldClock(['UTC', 'America/New_York', 'Asia/Tokyo'])
    data = clock.export_to_dict()
    
    import json
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    print("\n🌍 WORLD CLOCK - PYTHON EXAMPLES\n")

    example_1_simple_display()
    example_2_table_display()
    example_3_get_times()
    example_4_custom_timezones()
    example_5_add_remove_timezones()
    example_7_export_data()

    # Uncomment to run live clock:
    # example_6_live_clock()

    print("\n✅ All examples completed!")
