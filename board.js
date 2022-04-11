function Logedin(){
    console.log("tom")
    var Username = document.getElementById("Username").value

    var password = document.getElementById("password").value

    if(Username == "" && password == ""){
        alert("You are login successfully")

    }else{
        alert("Failed login")
    }
}
