function compute(){
    p = document.getElementById("principal").value;
    var principal = document.getElementById("principal").value;
    var rate = document.getElementById("rate").value;
    var years = document.getElementById("years").value;
    var interest = principal * years * rate /100;
    var year = new Date().getFullYear()+parseInt(years);

     //check if a principle is zero or less than zero
     if(principal == undefined || principal <= 0){
        alert("Please, enter a positive number");
        document.getElementById("principal").focus();
        return
    }
    //count and display
    else{
        var user_deposit = "If you deposit <mark>" + principal+",</mark><br>";
        var user_rate = "at an interest rate of <mark>" + rate+"%,</mark><br>";
        var user_interest = "You will receive an amount of <mark>"+ interest+",</mark><br>";
        var user_year = "in the year <mark'>" + year +"</mark>";

        document.getElementById("result").innerHTML=user_deposit+user_rate+user_interest+user_year;
    }
}
//update a rate
function updateRate(){
        var rateval = document.getElementById("rate").value;
        document.getElementById("rate_val").innerText=rateval;
        onchange="rate_val(this.value)"
}