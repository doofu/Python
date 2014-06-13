/**
 * 初始化页面
 */
function initPage() {
	// 显示错误信息
	errMessage();
	
	// 根据cookie中的值，设置username的值
	username = getCookie('username');
	$("#username").val(username);

	// 根据cookie中的值，设置checkbox的初始状态
	checked = getCookie('checked');

	if (checked == 'checked')
		$("#isChecked").attr('checked', 'yes');
	else
		$("#isChecked").removeAttr('checked');
}

/*
 * 取cookie值
 */
function getCookie(c_name) {
	//先查询cookie是否为空，为空就return ""
	if (document.cookie.length > 0) {
		//通过String对象的indexOf()来检查这个cookie是否存在，不存在就为 -1　　
		c_start=document.cookie.indexOf(c_name + "=")　　
　　　　　　
		if (c_start != -1) { 
			// 最后这个+1其实就是表示"="号啦，这样就获取到了cookie值的开始位置
			c_start = c_start + c_name.length + 1　　
			
			// 其实我刚看见indexOf()第二个参数的时候猛然有点晕，后来想起来表示指定的开始索引的位置...
			// 这句是为了得到值的结束位置。因为需要考虑是否是最后一项，所以通过";"号是否存在来判断
			c_end=document.cookie.indexOf(";", c_start)　　
			
			// 通过substring()得到了值。想了解unescape()得先知道escape()是做什么的，都是很重要的基础
			if (c_end == -1) c_end=document.cookie.length　　
				return unescape(document.cookie.substring(c_start, c_end))　　
		} 
	}
	
　　	return ""
}　　

/**
 * 使用JQuery，显示错误信息
 */
function errMessage() {
	var queryString = window.top.location.search.substring(1); 

	switch (getParameter(queryString, 'err')) {
		case '1':
			$("#errMessage").html("验证码不对");
			break;
		case '2':
			$("#errMessage").html("用户名为空");
			break;
		case '3':
			$("#errMessage").html("用户不存在");
			break;
		case '4':
			$("#errMessage").html("密码错");
			break;
	}
} 

/**
 * 从URL的GET方式传递的查询串中取某个值
 * @param queryString		查询串(url中?之后的部分，不含问号)
 * @param parameterName		要查询的名称
 * @returns					查询到的值
 */
function getParameter(queryString, parameterName) {  
	// Add "=" to the parameter name (i.e. parameterName=value)  
	var parameterName = parameterName + "=";  

	if (queryString.length > 0) {  
		// Find the beginning of the string  
		begin = queryString.indexOf(parameterName);  
		// If the parameter name is not found, skip it, otherwise return the value  
		if (begin != -1) {  
			// Add the length (integer) to the beginning  
			begin += parameterName.length;  
			// Multiple parameters are separated by the "&" sign  
			end = queryString.indexOf("&", begin);  
			if (end == -1) {  
				end = queryString.length  
			}  

			// Return the string  
            return unescape(queryString.substring(begin, end));  
		}
	}  

    // Return "null" if no parameter has been found  
    return "null";  
} 