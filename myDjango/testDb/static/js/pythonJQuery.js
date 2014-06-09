function getUserByGet() {
	// Get方式下，中文会产生乱码
	// 解决中文乱码问题的方法1,页面端发出的数据作一次encodeURI，服务端使用new
	// String(old.getBytes("iso8859-1"),"UTF-8");
	// 解决中文乱码问题的方法2,页面端发出的数据作两次encodeURI,服务端使用String name =
	// URLDecoder.decode(old,"UTF-8");
	
	var url = "jquerySearch?fn=getUser&username="
		+ encodeURI(encodeURI($("#username").val()));
		// var url = "../control/controler.php?fn=getUser&username=" +
	// $("#username").val();
	url = convertURL(url);
	
	$.ajax({
		type : "get", // 请求方式
		url : url, // 发送请求地址
		dataType : "xml", // 返回数据为xml格式
		data : { // 发送给数据库的数据
		},
		// 请求成功后的回调函数
		success : function(xml) {
			// 取XML数据中的数据项
			var age = $(xml).find("age").text();
			var salary = $(xml).find("salary").text();
			var phonenumber = $(xml).find("phonenumber").text();
			var email = $(xml).find("email").text();
			var password = $(xml).find("password").text();

			// 回填html中form相应的字段
			$("#age").val(age);
			$("#salary").val(salary);
			$("#phonenumber").val(phonenumber);
			$("#email").val(email);
			$("#password").val(password);
			$("#myres").html("");
		}
	});
}

function getUserByPost() {
	$.ajax({
		type : "post", // 请求方式
		url : "jquerySearch/?fn=getUser", // 发送请求地址
		dataType : "xml", // 返回数据为xml格式
		data : { // 发送给数据库的数据
			username : $("#username2").val(),
//			csrfmiddlewaretoken : $.cookie('csrftoken'),	// post方式下，必须传输csrfmiddlewaretoken
			csrfmiddlewaretoken : getCookie('csrftoken'),	// post方式下，必须传输csrfmiddlewaretoken
		},
		// 请求成功后的回调函数
		success : function(xml) {
			// 取XML数据中的数据项
			var age = $(xml).find("age").text();
			var salary = $(xml).find("salary").text();
			var phonenumber = $(xml).find("phonenumber").text();
			var email = $(xml).find("email").text();
			var password = $(xml).find("password").text();

			// 回填html中form相应的字段
			$("#age2").val(age);
			$("#salary2").val(salary);
			$("#phonenumber2").val(phonenumber);
			$("#email2").val(email);
			$("#password2").val(password);
			$("#myres2").html("");
		}
	});
}

// 给url地址增加时间差，瞒过浏览器，不读取缓存
function convertURL(url) {
	// 获取时间戳
	var timstamp = (new Date()).valueOf();
	// 将时间戳信息拼接到url上
	if (url.indexOf("?") >= 0) {
		url = url + "&t=" + timstamp;
	} else {
		url = url + "?t=" + timstamp;
	}
	return url;
}

function addUserByPost() {
	$.ajax({
		type : "post", // 请求方式
		url : "../control/controler.php?fn=addUser", // 发送请求地址
		data : { // 发送给数据库的数据
			username : $("#username").val(),
			age : $("#age").val(),
			salary : $("#salary").val(),
			phonenumber : $("#phonenumber").val(),
			email : $("#email").val(),
			password : $("#password").val(),
		},
		// 请求成功后的回调函数有两个参数
		success : function(data, textStatus) {
			$("#myres").html(data);
		}
	});
}

function deleteUserByPost() {
	$.ajax({
		type : "post", // 请求方式
		url : "../control/controler.php?fn=deleteUser", // 发送请求地址
		data : { // 发送给数据库的数据
			username : $("#username2").val()
		},
		// 请求成功后的回调函数有两个参数
		success : function(data, textStatus) {
			$("#myres2").html(data);
		}
	});
}

function modifyUserByPost() {
	$.ajax({
		type : "post", // 请求方式
		url : "../control/controler.php?fn=modifyUser", // 发送请求地址
		data : { // 发送给数据库的数据
			username : $("#username2").val(),
			age : $("#age2").val(),
			salary : $("#salary2").val(),
			phonenumber : $("#phonenumber2").val(),
			email : $("#email2").val(),
			password : $("#password2").val(),
		},
		// 请求成功后的回调函数有两个参数
		success : function(data, textStatus) {
			$("#myres2").html(data);
		}
	});
}

//使用jQuery，去cookie中的值
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
