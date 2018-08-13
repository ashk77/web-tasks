function myF()
{
	
let fname = document.getElementById("first-name").value
let lname = document.getElementById("last-name").value; 
let email = document.getElementById("email").value;
let pass = document.getElementById("pass").value;
let phone = document.getElementById("phone").value;

if(fname.length>15||fname[0]!=fname[0].toUpperCase())
{
	document.getElementById("error-fname").innerHTML="First name should be less than 15 characters"+
	" and start with a capital letter";
}
if(lname.length>15||lname[0]!=lname[0].toUpperCase())
{
	document.getElementById("error-lname").innerHTML="Last name should be less than 15 characters"+
	" and start with a capital letter";
}
if(email.search('@')<0)
{
	document.getElementById("error-email").innerHTML="Invalid E-mail Id";
}
//TODO : insert regex
// var pattern = ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15};
// if(pattern.test(pass))
// {
// 	document.getElementById("error-pass").innerHTML="Password should contain atleast 1 capital letter,"+
// 	" 1 small letter and 1 special character";
// }
if(phone>10e10||phone<999999999)
{
	document.getElementById("error-phone").innerHTML="Invalid Phone Number";
}

}