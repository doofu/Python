from urllib import parse
import math

#===============================================================================
# PagingToolbar 分页类
# @author  根据php代码修改而成
# @date 2014-6-11
# show(2)  1 ... 62 63 64 65 66 67 68 ... 150
# 分页样式（参见common.css）
# #page{font:12px/16px arial}
# #page span{float:left;margin:0px 3px;}
# #page a{float:left;margin:0 3px;border:1px solid #ddd;padding:3px 7px; text-decoration:none;color:#666}
# #page a.now_page,#page a:hover{color:#fff;background:#05c}
#===============================================================================
class PagingToolbar:
	request = {}				# 
	first_row = 0 				# 起始行数
	list_rows = 10 				# 列表每页显示行数
	total_pages = 0 			# 总页数
	total_rows = 0 				# 总行数
	now_page = 1				# 当前页数
	method = 'defalut' 			# 处理情况 Ajax分页 Html分页(静态化时) 普通get方式
	page_name = 'p' 			# 分页参数的名称，缺省为'p'
	ajax_func_name = ''			# 使用Ajax或JQuery时，调用的javascript函数的名称
	parameter = ''				# javascript函数的参数格式为'参数1,参数2,...,参数n'，
								# 自动调用javascript函数：ajax_func_name(当前页, 参数1, 参数2, ..., 参数n);
	plus = 4 					# 分页偏移量
	url = ''
	
	#==============================================================================
	# __init__ 构造函数
	# @param 列表 data
	#==============================================================================
	def __init__(self, data = {}):
		self.request = data ['request']
		self.total_rows = int ( data ['total_rows'] )
		self.parameter = data.get( 'parameter', '' )
		self.list_rows = int ( data.get( 'list_rows', '15' ) )
		
		self.total_pages = math.ceil ( self.total_rows / self.list_rows )
		
		self.page_name = data.get('page_name', 'p')
		self.ajax_func_name = data.get('ajax_func_name', '')
		
		self.method = data.get('method', '')
		
		# 当前页面
		self.now_page = int(data.get('now_page', self.request.GET.get(self.page_name, '1')))

		self.now_page = 1 if (self.now_page <= 0) else self.now_page
		
		if  self.total_pages  and (self.now_page > self.total_pages):
			self.now_page = self.total_pages

		self.first_row = self.list_rows * (self.now_page - 1);
	
	#==============================================================================
	# _get_link 得到当前连接
	# @param	int page
	# @param	text
	# @return 	string	
	#==============================================================================
	def _get_link(self, page, text):
		print(self.method)
		if self.method == 'ajax' :
			print('enter ajax')
			parameter = ''
			if self.parameter:
				parameter = ',' + self.parameter

			return '<a onclick="' + self.ajax_func_name + '(\'' + str(page) + '\'' + parameter + ')" href="javascript:void(0)">' + text + '</a>' + "\n"

		elif self.method == 'html' :
			url = self.parameter.replace ( '?', str(page) )
			return '<a href="' + url + '">' + text + '</a>' + '\n'
			
		else:
			return '<a href="' + self._get_url ( page ) + '">' + text + '</a>' + '\n'
	
	#==============================================================================
	# _set_url 设置当前页面链接
	#==============================================================================
	def _set_url(self):
		url = self.request.get_full_path() + ('' if '?' in self.request.get_full_path() else '?') + self.parameter
		parse1 = parse.urlparse(url)  # php: parse = parse_url ( url )-----------
		params = ''
		if (parse1.query):
			params = dict([x.split("=") for x in parse1.query.split("&")])  # 返回一个字典
			#cgi.parse_qsl(parse.query)	# php: parse_str ( $parse ['query'], $params );
			del params[self.page_name] # php: unset ( $params [$this->page_name] );
			
			url = ''
			for key in params:
				url += ('&' if url else '') + key + '=' + params[key]
			url = parse1.path + '?' + url

		if params:
			url += '&'

		self.url = url
	
	#==============================================================================
	# _get_url 得到page的url
	# @param int page 页面        	
	# @return string
	#==============================================================================
	def _get_url(self, page):
		if not self.url:
			self._set_url ()

		# $lable = strpos('&', $this->url) === FALSE ? '' : '&';
		return self.url + self.page_name + '=' + str(page)
	
	#==============================================================================
	# first_page 得到第一页
	# @return string
	#==============================================================================
	def first_page(self, name = '第一页'):
		if (self.now_page > 5):
			return self._get_link ( '1', name )

		return ''

	#==============================================================================
	# last_page 最后一页
	# @param	name
	# @return string
	#==============================================================================
	def last_page(self, name = '最后一页'):
		if (self.now_page < self.total_pages - 5):
			return self._get_link ( self.total_pages, name );

		return ''
	
	#==============================================================================
	# up_page 上一页
	# @return string
	#==============================================================================
	def up_page(self, name = '上一页'):
		if (self.now_page != 1):
			return self._get_link ( self.now_page - 1, name )

		return ''
	
	#==============================================================================
	# down_page 下一页
	# @return string
	#==============================================================================
	def down_page(self, name = '下一页'):
		if (self.now_page < self.total_pages):
			return self._get_link ( self.now_page + 1, name )

		return ''

	#==============================================================================
	# goto_page 输入页面，直接跳转控件
	# @return string
	#==============================================================================
	def goto_page(self, name = 'Go'):
		ret = '<form><input type="text" value="' + str(self.now_page) + '" id="gotoPage" size="3" class="gotoPageInput">'
		ret += '<input type="button" onclick="' + self.ajax_func_name + '(gotoPage.value' + ',' + str(self.list_rows) 
		ret += ',' + str(self.total_rows) + ')" value="' + name + '" class="gotoButton"></form>'

		return ret;
	
	#==============================================================================
	# select_page 页面选择控件
	# @return string
	#==============================================================================
	def select_page(self):
		if (self.plus + self.now_page > self.total_pages):
			begin = self.total_pages - self.plus * 2;
		else:
			begin = self.now_page - self.plus;

		begin = begin if begin >= 1 else 1
		
		ret = '<select onchange="' + self.ajax_func_name + '(this.value' + ',' + str(self.list_rows) + ',' + str(self.total_rows) + ')" class="gotoPageSelect">'
		
		for i in range(begin, begin + 11):          #for (i = begin; i <= begin + 10; i ++):
			if i > self.total_pages:
				break;
			if i == self.now_page:
				ret += '<option selected="true" value="' + str(i) + '">' + str(i) + '</option>';
			else:
				ret += '<option value="' + str(i) + '">' + str(i) + '</option>';

		ret += '</select>'
		
		return ret

	#==============================================================================
	# message_page 统计信息显示控件
	# @return string
	#==============================================================================
	def message_page(self):
		ret = '<span class="messagePage">总计' + str(self.total_rows) + '条' + str(self.total_pages) + '页'
		ret += ',每页' + str(self.list_rows) + '条, 当前第' + str(self.now_page) + '页</span>'
#		return .= '<input type="text" value="' . $this->list_rows . '" id="pageSize" size="3"> ';

		return ret
	
	#==============================================================================
	# show 分页样式输出
	# @param	$param
	# @return string
	#==============================================================================
	def show(self, param = 1):
		if (self.total_rows < 1):
			return ''
		
		if param == 1:
			return self.show_1()
		elif param == 2:
			return self.show_2()
		elif param == 3:
			return self.show_3()
		elif param == 4:
			return self.show_4()
		else:
			return ''
		
	#==============================================================================
	# show_1 方式一
	#==============================================================================
	def show_1(self):
		plus = self.plus
		
		if plus + self.now_page > self.total_pages:
			begin = self.total_pages - plus * 2
		else:
			begin = self.now_page - plus

		
		begin = begin if begin >= 1 else 1
		ret = ''
		ret += self.first_page ()
		ret += self.up_page ()
		#for($i = $begin; $i <= $begin + $plus * 2; $i ++) {
		for i in range(begin, begin + plus * 2 + 1):
			if i > self.total_pages:
				break

			if i == self.now_page:
				ret += '<a class="now_page">' + str(i) + '</a>\n'
			else:
				ret += self._get_link ( i, str(i) ) + "\n"

		ret += self.down_page ()
		ret += self.last_page ()

		return ret
			
	#==============================================================================
	# show_2 方式二
	#==============================================================================
	def show_2(self):
		ret = ''
		
		if self.total_pages != 1:
			ret += self.up_page ( '<' )

			for i in range(1, self.total_pages + 1):											
				if i == self.now_page:
					ret += '<a class="now_page">' + str(i) + '</a>\n'
				else:
					if (self.now_page - i >= 4) and i != 1:
						ret += "<span class='pageMore'>...</span>\n"
						i = self.now_page - 3
					else:
						if  (i >= self.now_page + 5) and (i != self.total_pages):
							ret += "<span>...</span>\n"
							i = self.total_pages
						ret += self._get_link ( i, str(i) ) + "\n"
			ret += self.down_page ( '>' )
			
		return ret
	

	#==============================================================================
	# show_3 方式三
	#==============================================================================
	def show_3(self):
		ret = self.message_page()
		ret += self.first_page () + "\n"
		ret += self.up_page () + "\n"
		ret += self.down_page () + "\n"
		ret += self.last_page () + "\n"
		ret += self.select_page()
		
		return ret

	#==============================================================================
	# show_4 方式四
	#==============================================================================
	def show_4(self):
		# 显示方法一的控件
		ret = self.show_1()
		# 显示选择控件		
		ret += self.select_page()
		# 显示页面跳转控件
		ret += self.goto_page()
		
		ret += self.message_page()
		
		return ret
