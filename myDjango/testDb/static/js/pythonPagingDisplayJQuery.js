// 分页显示数据
function getPagingData(pageNow, listRows, totalRows) {
	// 如果当前页超出最后一页，设为最后一页
	if ((pageNow -1) * listRows > totalRows)
		pageNow = Math.floor(totalRows / listRows) + 1;

	// 显示表格数据
	$.ajax({
		type : "post", // 请求方式
		url : "pagingDisplayJQuery/pagingDisplayJQuery/", // 发送请求地址
		dataType : "xml", // 返回数据为xml格式
		data : { // 发送给数据库的数据
			fn : "getPagingData",
			pageNow : pageNow,
			listRows: listRows,
			csrfmiddlewaretoken : getCookie('csrftoken'),	// post方式下，必须传输csrfmiddlewaretoken
		},
		// 请求成功后的回调函数
		success : function(xml) {
			i=0;
			$(xml).find("users").find("user").each(function(){

				var name=$(this).children("name").text();
				var age=$(this).children("age").text();
				var salary=$(this).children("salary").text();
				var phonenumber=$(this).children("phonenumber").text();
				var email=$(this).children("email").text();
				var password=$(this).children("password").text();
				
				// 回填html中form相应的字段
				eval("$('#data"+i+"_0').html(name)");
				eval("$('#data"+i+"_1').html(age)");
				eval("$('#data"+i+"_2').html(salary)");
				eval("$('#data"+i+"_3').html(phonenumber)");
				eval("$('#data"+i+"_4').html(email)");
				eval("$('#data"+i+"_5').html(password)");

				i = i + 1;
			});
			
			while (i < listRows) {
				eval("$('#data"+i+"_0').html('')");
				eval("$('#data"+i+"_1').html('')");
				eval("$('#data"+i+"_2').html('')");
				eval("$('#data"+i+"_3').html('')");
				eval("$('#data"+i+"_4').html('')");
				eval("$('#data"+i+"_5').html('')");
				
				i = i + 1;
			}
		}
	});
	
	// 显示分页工具条
	showPagingToolbar(pageNow, listRows, totalRows);
}

// 显示分页工具条
function showPagingToolbar(pageNow, listRows, totalRows){  
	$.ajax({
		type : "post", // 请求方式
		url : "pagingDisplayJQuery/showPagingToolbar/", // 发送请求地址
		dataType : "html", // 返回数据为html格式
		data : { // 发送给数据库的数据
			fn : "getPagingToolBar",
			totalRows: totalRows,
			pageNow : pageNow,
			listRows: listRows,
			csrfmiddlewaretoken : getCookie('csrftoken'),	// post方式下，必须传输csrfmiddlewaretoken
		},
		// 请求成功后的回调函数
		success : function(pagingBar) {
			$('#pagingToolbar').html(pagingBar);
//			$('#page').html(pagingBar);
		}
	});
}

// 第一次刷新页面时，显示分页数据
function afterLoad(pageNow, listRows, totalRows){   
	var s = document.readyState;    
	if(s=="complete"){
		getPagingData(pageNow, listRows, totalRows);
	}
}