# 😂 Random Joke Generator

A fun and interactive random joke generator using the free **JokeAPI**. Multiple implementations available for different platforms.

## 📋 Table of Contents
- [Features](#features)
- [API Details](#api-details)
- [Implementations](#implementations)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Categories](#categories)
- [API Response Format](#api-response-format)
- [Troubleshooting](#troubleshooting)

---

## ✨ Features

✅ **No API Key Required** - Completely free public API  
✅ **Multiple Categories** - Programming, Pun, Knock-Knock, Dark, General, etc.  
✅ **Safe Mode** - Filter offensive content  
✅ **Single & Two-Part Jokes** - Setup and punchline support  
✅ **Fast & Reliable** - Tested daily, always working  
✅ **Multiple Implementations** - HTML, JavaScript, Python, React  
✅ **Responsive Design** - Works on mobile and desktop  
✅ **No Dependencies** - Pure vanilla implementations  

---

## 🔌 API Details

**API Name:** JokeAPI by Sv443  
**Base URL:** `https://v2.jokeapi.dev/joke`  
**Authentication:** None required  
**Rate Limit:** Generous (suitable for most use cases)  
**Documentation:** https://jokeapi.dev/

### Endpoints

```
GET /joke/{category}                    # Get joke from specific category
GET /joke/{category}?safe-mode          # Safe mode enabled
GET /joke/Any                           # Random category
GET /joke/Programming                   # Programming jokes
GET /joke/Pun                          # Pun jokes
GET /joke/Knock-Knock                  # Knock-knock jokes
GET /joke/Dark                         # Dark humor
```

---

## 🛠️ Implementations

### 1. **HTML/JavaScript (Interactive Web App)**
- **File:** `joke-generator-html/index.html`
- **Features:** Full UI, category selection, safe mode toggle, punchline reveal
- **How to use:** Open in browser
- **Dependencies:** None

**Live Features:**
- Category selector dropdown
- Safe mode checkbox
- Dynamic punchline reveal
- Joke counter
- Loading animation
- Error handling

---

### 2. **JavaScript Module (Node.js/Browser)**
- **File:** `joke-generator-js/index.js`
- **Features:** Reusable module, supports Node.js and browsers
- **How to use:** Import and use in your project

```javascript
// Browser usage
<script src="joke-generator-js/index.js"></script>
<script>
  JokeGenerator.getJoke('Programming').then(joke => {
    console.log(JokeGenerator.formatJoke(joke));
  });
</script>

// Node.js usage
const JokeGenerator = require('./joke-generator-js/index.js');
JokeGenerator.getJoke().then(joke => console.log(joke));
```

---

### 3. **Python Script**
- **File:** `joke-generator-python/joke_generator.py`
- **Features:** Class-based, multiple examples, batch processing
- **How to use:** `python joke_generator.py`
- **Dependencies:** `requests` library

```bash
pip install requests
python joke-generator-python/joke_generator.py
```

**Includes Examples:**
- Single joke
- Multiple jokes
- Random category
- Interactive mode
- Batch processing to JSON

---

### 4. **React Component**
- **File:** `joke-generator-react/JokeGenerator.jsx` + `JokeGenerator.css`
- **Features:** React hooks, responsive design
- **How to use:** Import into your React app

```jsx
import JokeGenerator from './joke-generator-react/JokeGenerator';

export default function App() {
  return <JokeGenerator />;
}
```

---

## 🚀 Quick Start

### HTML/JavaScript (Easiest)
1. Open `joke-generator-html/index.html` in your browser
2. Click "Get Joke"
3. Click "Show Punchline" for two-part jokes
4. Select category or enable safe mode as desired

### Python
```bash
# Install requirements
pip install requests

# Run the generator
python joke-generator-python/joke_generator.py
```

### JavaScript (Node.js)
```javascript
// Copy the code from joke-generator-js/index.js
// Or in Node.js:
const fetch = require('node-fetch');
const JokeGenerator = require('./joke-generator-js/index.js');

JokeGenerator.getJoke('Programming').then(joke => {
  console.log(joke);
});
```

### React
```bash
# Install in your React project
npm install

# Copy JokeGenerator.jsx and JokeGenerator.css to your components folder

# Use in your app
import JokeGenerator from './components/JokeGenerator';
```

---

## 📚 Usage Examples

### Example 1: Get a Single Joke (JavaScript)
```javascript
async function tellJoke() {
  const joke = await JokeGenerator.getJoke('Programming', true);
  console.log(JokeGenerator.formatJoke(joke));
}

tellJoke();
```

### Example 2: Get Multiple Jokes (Python)
```python
from joke_generator import JokeGenerator

generator = JokeGenerator(safe_mode=True)
jokes = generator.get_multiple_jokes(count=5, category='Pun')

for joke in jokes:
    generator.print_joke(joke, show_metadata=True)
```

### Example 3: Interactive Selection (Python)
```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
category = generator.get_random_category()
joke = generator.get_joke(category)
generator.print_joke(joke, show_metadata=True)
```

### Example 4: Fetch in React
```jsx
const [joke, setJoke] = useState(null);

const fetchJoke = async () => {
  const response = await fetch('https://v2.jokeapi.dev/joke/Programming');
  const data = await response.json();
  setJoke(data);
};

return (
  <div>
    <button onClick={fetchJoke}>Get Joke</button>
    {joke && <p>{joke.joke || joke.setup}</p>}
  </div>
);
```

---

## 🎭 Categories

| Category | Description | Example |
|----------|-------------|---------|
| **Any** | Random from all categories | Mixed |
| **Programming** | IT & coding jokes | "Why do programmers prefer dark mode?" |
| **Pun** | Wordplay jokes | "I'm reading a book on the history of glue..." |
| **Knock-Knock** | Classic knock-knock jokes | "Knock knock!" |
| **General** | General humor | Various |
| **Dark** | Dark/adult humor | Requires unsafe mode |

---

## 📊 API Response Format

### Single Joke Response
```json
{
  "category": "Programming",
  "type": "single",
  "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
  "flags": {
    "nsfw": false,
    "religious": false,
    "political": false,
    "racist": false,
    "sexist": false,
    "explicit": false
  },
  "id": 6,
  "safe": true,
  "error": false
}
```

### Two-Part Joke Response
```json
{
  "category": "Programming",
  "type": "twopart",
  "setup": "How many programmers does it take to change a lightbulb?",
  "delivery": "None, that's a hardware problem!",
  "flags": { ... },
  "id": 7,
  "safe": true,
  "error": false
}
```

---

## 🔧 Customization

### Add Custom Categories
```javascript
// JavaScript
const customCategories = ['Programming', 'Pun', 'Custom'];
category = customCategories[Math.floor(Math.random() * customCategories.length)];
```

### Filter by Flags
```python
# Python - filter explicit jokes
joke = generator.get_joke('Any')
if not joke.get('flags', {}).get('explicit', False):
    generator.print_joke(joke)
```

### Styling (HTML)
Edit the `<style>` section in `joke-generator-html/index.html` to customize colors, fonts, and layout.

---

## 🐛 Troubleshooting

### Issue: "No jokes available for this category"
- **Solution:** Try a different category or use 'Any'
- **Cause:** Some categories may be temporarily unavailable

### Issue: CORS Error (Browser)
- **Solution:** Use a CORS proxy or server-side solution
- **Note:** JokeAPI supports CORS, should work in modern browsers

### Issue: API Timeout
- **Solution:** Add timeout handling in your requests
- **Cause:** Network issues or rate limiting

### Issue: Punchline not showing
- **Solution:** Check if `joke.type === 'twopart'`
- **Cause:** Single jokes don't have punchlines

---

## 📦 Dependencies

| Implementation | Dependencies | Size |
|---|---|---|
| HTML/JS | None | ~50 KB |
| JavaScript | None (Node 18+) | ~5 KB |
| Python | `requests` | ~10 KB |
| React | React 16.8+ | ~15 KB |

---

## 🔐 Privacy & Security

✅ **No Personal Data Collected**  
✅ **No API Key Storage Required**  
✅ **HTTPS Encrypted**  
✅ **No Tracking**  
✅ **Open Source API**

---

## 📄 License

This project uses the free **JokeAPI** by Sv443 (MIT License).

---

## 🎯 Future Enhancements

- [ ] Voice output (text-to-speech)
- [ ] Joke sharing to social media
- [ ] Favorite jokes saved locally
- [ ] Multilingual support
- [ ] Mobile app version
- [ ] Integration with Discord bot
- [ ] Scheduled joke notifications

---

## 🤝 Contributing

Want to improve this project? Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 📞 Support

- **API Issues:** Visit https://github.com/Sv443-Network/JokeAPI/issues
- **This Project:** Check the repository issues
- **Questions:** Create a new issue with your question

---

## 🙏 Credits

- **JokeAPI** by Sv443 - Free public joke API
- Inspired by various joke generator projects

---

**Enjoy the laughs! 😂**
