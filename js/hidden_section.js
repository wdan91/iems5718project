function clearit(url) {
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
}

function submit() {
    var url = 'hidden_section/login';
    postdata =  "from=ajax" + "&username=" + $('#username').val()
                            + "&password=" + $('#password').val();
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

function ok() {
    var url = 'hidden_section';
    postdata =  "";
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
            }
        }
    }
}