module.exports = {
  content: ['app/core/templates/index.html','app/core/templates/login.html','app/core/templates/forget.html'],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/typography"),require("daisyui"),
  ],
   // daisyUI config (optional)
   daisyui: {
    styled: true,
    themes: true,
    base: true,
    utils: true,
    logs: true,
    rtl: false,
    prefix: "",
    darkTheme: "dark",
  },
}
