function message_error(obj) {
	var html;
	$.each(obj, function(key, value) {
		html=  value;
	});
	Toast.fire({
		icon: 'error',
		title: html
	});

}

function message_success(message) {
	Toast.fire({
		icon: 'success',
		title: message
	});

}
