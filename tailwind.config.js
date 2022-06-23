/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/core/templates/test.html",
    "./app/core/templates/forget.html",
    "./app/core/templates/index.html",
    "./app/core/templates/login.html",
    "./app/core/templates/password.html",
    "./app/core/templates/signup.html",
  


],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}
