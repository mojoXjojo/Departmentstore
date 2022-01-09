function validateF()
{
var name=document.regiserForm.Fname.value;
var email=document.regiserForm.email.value;
var mob=document.regiserForm.Mobile.value;
var pass1=document.regiserForm.pass1.value;
var pass2=document.regiserForm.pass2.value;

console.log(name);
if((Uname=" ") || (email=" ") || (mob=" ") || (pass1=" ") || (pass2=" "))
{
alert("Please input the empty fields");
return false;
}
}

function confirm()
{
var pass1=document.registerForm.pass1.value;
var pass2=document.registerForm.pass2.value;
if(pass1!= pass2)
	{
	alert("Password is not same");
	return false;
	}
}

function mob()
{
var Mobile;
Mobile=document.registerForm.Mobile.value;
if(isNAN(Mobile)||(Mobile<=0)||(Mobile>10))
	{
	alert("Enter the correct mobile number");
	return false;
	}
}