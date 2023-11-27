
console.log('eye.js');  
const passwordToggle = document.querySelector('.js-password-toggle')

passwordToggle.addEventListener('change', function() {
  console.log('change');
  const password = document.querySelector('.js-password'),
    passwordLabel = document.querySelector('.js-password-label')
    console.log('hewllo')

  if (password.type === 'password') {
    password.type = 'text'
    passwordLabel.innerHTML = '<i class="fa-solid fa-eye fa-sm" ></i> '
  } else {
    password.type = 'password'
    passwordLabel.innerHTML = '<i class="fa-solid fa-eye-slash fa-sm"></i> '
  }

  password.focus()
});
