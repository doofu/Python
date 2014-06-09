// 创建ajax引擎
function getXmlHttpObject() {
	var xmlHttpRequest;

	// 不同浏览器获取对象xmlHttpRequest方法不一样
	if (window.ActiveXObject) {
		xmlHttpRequest = new ActiveXObject("Microsoft.XMLHTTP");
	} else {
		xmlHttpRequest = new XMLHttpRequest();
	}
	return xmlHttpRequest;
}

var myXmlHttpRequest = "";

// 使用Get方式，验证用户名是否存在
function getPhoneNumberByGet() {

	myXmlHttpRequest = getXmlHttpObject();

	// 怎么判断创建ok
	if (myXmlHttpRequest) {

		// 通过myXmlHttpRequest对象发送请求到服务器的某个页面
		// 第一个参数表示请求的方式, "get" / "post"
		// 第二个参数指定url,对哪个页面发出ajax请求(本质仍然是http请求)
		// 第三个参数表示 true表示使用异步机制,如果false表示不使用异步
		// Get方式下，中文会产生乱码
		// 解决中文乱码问题的方法1,页面端发出的数据作一次encodeURI，服务端使用new
		// String(old.getBytes("iso8859-1"),"UTF-8");
		// 解决中文乱码问题的方法2,页面端发出的数据作两次encodeURI,服务端使用String name =
		// URLDecoder.decode(old,"UTF-8");

		var url = "ajaxSearch?fn=getPhonenumber&mytime="
				+ new Date() + "&username="
				+ encodeURI(encodeURI($("username").value));

		// 打开请求.
		myXmlHttpRequest.open("get", url, true);

		// 指定回调函数.chuli是函数名
		myXmlHttpRequest.onreadystatechange = chuli;

		// 真的发送请求,如果是get请求则填入 null即可
		// 如果是post请求，则填入实际的数据
		myXmlHttpRequest.send(null);
	}
}

// 回调函数
function chuli() {

	// window.alert("处理函数被调回" + myXmlHttpRequest.readyState);
	// 我要取出从registerPro.php页面返回的数据
	if (myXmlHttpRequest.readyState == 4) {

		// 取出值,根据返回信息的格式定.text
		// window.alert("服务器返回："+myXmlHttpRequest.responseText);

		$('myres').value = myXmlHttpRequest.responseText;
	}
}

// 使用Post方式，验证用户名是否存在
function getPhoneNumberByPost() {
	myXmlHttpRequest = getXmlHttpObject();

	// 怎么判断创建ok
	if (myXmlHttpRequest) {

		// 通过myXmlHttpRequest对象发送请求到服务器的某个页面
		// 第一个参数表示请求的方式, "get" / "post"
		// 第二个参数指定url,对哪个页面发出ajax请求(本质仍然是http请求)
		// 第三个参数表示 true表示使用异步机制,如果false表示不使用异步
		var url = "ajaxSearch/?fn=getPhonenumber";						// 重要：注意，post方式，ajaxSearch后面的"/"一定要有！！
		var queryString = "mytime=" + new Date() + "&username="
				+ $("username2").value
				+ "&csrfmiddlewaretoken=" + getCookie('csrftoken');		// post方式下，必须传输csrfmiddlewaretoken

		// 打开请求.
		myXmlHttpRequest.open("post", url, true);

		// 指定回调函数.chuli是函数名
		myXmlHttpRequest.onreadystatechange = chuliPost;

		// 这句话不能少
		myXmlHttpRequest.setRequestHeader("Content-Type",
				"application/x-www-form-urlencoded");

		// 真的发送请求,如果是get请求则填入 null即可
		// 如果是post请求，则填入实际的数据
		myXmlHttpRequest.send(queryString);
	}
}

function chuliPost() {

	// window.alert("处理函数被调回" + myXmlHttpRequest.readyState);
	// 我要取出从registerPro.php页面返回的数据
	if (myXmlHttpRequest.readyState == 4) {

		// 取出值,根据返回信息的格式定.text
		// window.alert("服务器返回："+myXmlHttpRequest.responseText);

		$('myres2').value = myXmlHttpRequest.responseText;
	}
}

function $(id) {
	return document.getElementById(id);
}

// 使用jQuery，去cookie中的值
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
