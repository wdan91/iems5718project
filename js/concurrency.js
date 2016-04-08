function buyit(url) {
    var url = 'concurrency/buy';
    postdata =  "from=ajax" + "&qty1=" + $('#QTY1').val()
                            + "&qty2=" + $('#QTY2').val()
                            + "&qty3=" + $('#QTY3').val()
                            + "&qty4=" + $('#QTY4').val()
                            + "&total=" + $('#total').val();
    console.log(postdata);
    if (typeof XMLHttpRequest != 'undefined') {
        req = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        req = new ActiveXObject('Microsoft.XMLHTTP');
    }
    req.open('POST', url, true);
    req.onreadystatechange = callback;
    req.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    req.send(postdata);

    function callback() {
        if (req.readyState == 4) {
            if (req.status == 200) {
                var message = req.responseText;
                console.log(message);
                eval(message);
            }
        }
    }
}


function lockit(url) {
    document.getElementById('QTY1').disabled = true;
    document.getElementById('QTY2').disabled = true;
    document.getElementById('QTY3').disabled = true;
    document.getElementById('QTY4').disabled = true;
    var url = url + "?from=ajax&qty1=" + $('#QTY1').val()
                            + "&qty2=" + $('#QTY2').val()
                            + "&qty3=" + $('#QTY3').val()
                            + "&qty4=" + $('#QTY4').val();
    if (typeof XMLHttpRequest != 'undefined') {
        req = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        req = new ActiveXObject('Microsoft.XMLHTTP');
    }
    req.open('GET', url, true);
    req.onreadystatechange = callback;
    req.send(null);

    function callback() {
        if (req.readyState == 4) {
            if (req.status == 200) {
                var message = req.responseText;
                console.log(message);
                eval(message);
            }
        }
    }
}


function validate(url) {
    temp = document.getElementById('QTY1').value;
    if(temp==null || temp=="" || isNaN( temp )) 
        document.getElementById('QTY1').value='0';
    temp = document.getElementById('QTY2').value
    if(temp==null || temp=="" || isNaN( temp )) 
        document.getElementById('QTY2').value='0';
    temp = document.getElementById('QTY3').value
    if(temp==null || temp=="" || isNaN( temp )) 
        document.getElementById('QTY3').value='0';
    temp = document.getElementById('QTY4').value
    if(temp==null || temp=="" || isNaN( temp )) 
        document.getElementById('QTY4').value='0';
    //var url = url + "&from=ajax&key=' + encodeURIComponent(keyField.value)";
    var url = url + "?from=ajax&qty1=" + $('#QTY1').val()
                            + "&qty2=" + $('#QTY2').val()
                            + "&qty3=" + $('#QTY3').val()
                            + "&qty4=" + $('#QTY4').val();
    if (typeof XMLHttpRequest != 'undefined') {
        req = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        req = new ActiveXObject('Microsoft.XMLHTTP');
    }
    req.open('GET', url, true);
    req.onreadystatechange = callback;
    req.send(null);

    function callback() {
        if (req.readyState == 4) {
            if (req.status == 200) {
                var message = req.responseText;
                eval(message);
                console.log(message);
            }
        }
    }
}
