from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Portfolio</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f3f3f3;
        }

        nav {
            background: #222;
            color: white;
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav a {
            color: #ddd;
            margin-left: 20px;
            text-decoration: none;
            font-size: 18px;
        }

        nav a:hover {
            color: #ffcc00;
        }

        .logo {
            font-size: 22px;
            font-weight: bold;
        }

        .hero {
            text-align: center;
            padding: 80px 20px;
        }

        .hero h1 {
            font-size: 45px;
        }

        .hero h1 span {
            color: #ff6600;
        }

        .hero p {
            color: #444;
            font-size: 20px;
        }

        .btn {
            display: inline-block;
            padding: 12px 25px;
            background: #ff6600;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin-top: 20px;
        }

        .btn:hover {
            background: #cc5200;
        }

        /* Projects Section */
        .projects {
            padding: 60px 20px;
            background: white;
            text-align: center;
        }

        .projects h2 {
            font-size: 35px;
            color: #222;
        }

        .project-card {
            background: #ffffff;
            margin: 20px auto;
            padding: 20px;
            width: 60%;
            border-radius: 10px;
            box-shadow: 0 0 10px #ccc;
        }

        .project-card h3 {
            margin: 0;
            color: #ff6600;
        }

        .project-card p {
            color: #555;
        }
    </style>

</head>
<body>

<nav>
    <h2 class="logo">My Portfolio</h2>
    <div class="nav-links">
        <a href="/">Home</a>
        <a href="/about">About</a>
    </div>
</nav>

<section class="hero">
    <h1>Hello, I'm <span>Muskan Khan</span></h1>
    <p>Welcome to my portfolio website! I develop modern and clean Python applications.</p>
    <a href="/about" class="btn">About Me</a>
</section>

<!-- PROJECTS SECTION -->
<section class="projects">
    <h2>My Python Projects</h2>

    <div class="project-card">
        <h3>🧮 Unit Converter + Calculator</h3>
        <p>A Python CLI tool that converts units like km→miles, Celsius→Fahrenheit, speeds, time, and performs basic arithmetic.</p>
    </div>

    <div class="project-card">
        <h3>📊 Streamlit Dashboard</h3>
        <p>A simple dashboard built with Streamlit displaying data, charts, and interactive inputs.</p>
    </div>

    <div class="project-card">
        <h3>🎮 XO Game (Pygame)</h3>
        <p>A fun Tic-Tac-Toe game built using Python's Pygame library with interactive UI.</p>
    </div>

</section>

</body>
</html>
    """

    
@app.route("/about")
def about():
    return """
    <!DOCTYPE html>
<html>
<head>
    <title>About Me</title>

    <style>
        body {
            font-family: Arial;
            background: #e6e6e6;
            margin: 0;
            padding: 0;
        }
        header {
            background: #4CAF50;
            color: white;
            font-size: 28px;
            text-align: center;
            padding: 15px;
        }
        nav {
            background: #333;
            padding: 14px;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 15px;
            text-decoration: none;
            font-size: 18px;
        }
        nav a:hover {
            color: #4CAF50;
        }
        .about-container {
            background: white;
            width: 70%;
            margin: 30px auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        h2 {
            color: #4CAF50;
        }
        .skills {
            margin-top: 20px;
        }
        .skills li {
            margin-bottom: 8px;
            font-size: 18px;
        }
    </style>

</head>
<body>

<header>About Me – Muskaan Khan</header>

<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
</nav>

<div class="about-container">
    
    <h2>Who Am I?</h2>
    <p>
        I am Muskaan Khan, a B.Tech student specializing in AI & ML.
        I love creating Python projects, dashboards, automation tools, and working on real-world applications.
    </p>

    <h2>My Skills</h2>
    <ul class="skills">
        <li>✔ Python Programming</li>
        <li>✔ Streamlit Dashboard Development</li>
        <li>✔ Pygame Game Development</li>
        <li>✔ Presentation (PPT) Making</li>
        <li>✔ Basic Machine Learning</li>
        <li>✔ HTML & CSS (Beginner)</li>
    </ul>

</div>

</body>
</html>
    """

    
if __name__ =='__main__':
    app.run()
