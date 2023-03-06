function Login(){
    var fm = document.getElementById("fm");
    if(fm.id.value ==""){
        alert("input ID");
        fm.id.focus();
        return;
    }
    alert(fem.id.value);
}

function pw(){
    var fm = document.getElementById("fm");
    if(fm.pw.value ==""){
        alert("input PW");
        fm.pw.focus();
        return;
    }
    alert(fem.pw.value);
}

fm.action = "";
fm.submit();