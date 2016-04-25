function clearit(url) {
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
}

function getCookie(cname)
{
var name = cname + "=";
var ca = document.cookie.split(';');
for(var i=0; i<ca.length; i++) 
  {
  var c = ca[i].trim();
  if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
return "";
}

function setCookie(cname,cvalue) {
    var d = new Date();
    d.setTime(d.getTime()+(1*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
    return cvalue-1;
}

function submit() {
    if(0==getCookie('trynum')) {
        alert("You have tried too many times!");
        return;
    }
    setCookie('trynum',getCookie('trynum')-1);
    var url = 'cookie_change/login';
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
    var url = 'cookie_change';
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