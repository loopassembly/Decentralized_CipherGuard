// const { error } = require("daisyui/src/colors");

function clearErrors(){

    errors = document.getElementsByClassName('formerror');
    for(let item of errors)
    {
        item.innerHTML = "";
    }
}

function test(name,email,password,cpasword){
    document.forms['Rform']["username"].value=name;
    document.forms['Rform']["email"].value=email;
    document.forms['Rform']["password1"].value=password;
    document.forms['Rform']["password2"].value=cpasword;
}

function validateForm(event){
    var returnval = true;
    clearErrors();

    //perform validation and if validation fails, set the value of returnval to false
    var name = document.forms['Rform']["username"].value;
    console.log(name);
    if (name.length<5){
        event.preventDefault();
        document.getElementById("Euser").innerHTML = "Username must be at least 5 characters long";
       
        returnval = false;
    }

    if (name.length == 0){
        event.preventDefault();
        document.getElementById("Euser").innerHTML = "*Length of name cannot be zero!";
       
        returnval = false;
    }

    var email = document.forms['Rform']["email"].value;
    
    if (email.length== 0){
        event.preventDefault();
        document.getElementById("Eemail").innerHTML = "*Email is required";
       
        returnval = false;
    }
  



    var password = document.forms['Rform']["password1"].value;
    console.log(password)
    if (password.length < 6){
        
        event.preventDefault();
        document.getElementById("Epass1").innerHTML = "*Password should be atleast 6 characters long!";
        returnval = false;
    }

    var cpassword = document.forms['Rform']["password2"].value;
    
    if (cpassword != password){
        event.preventDefault();
        document.getElementById("Epass2").innerHTML = "**Password and Confirm password should match!";
        returnval = false;
    }

   
    if (returnval == true){ 
        console.log('all pas')//if all validation passes, submit the form
        test(name,email,password,cpassword);

    }
    
}

