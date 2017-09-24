$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

	$('#buttonId').click(function() {
		url = "{% url 'projects:projectSubscribe' 0 %}".replace('0', id_number);

	    $.ajax({
	        url: 'proje',
	        method: 'GET', // or another (GET), whatever you need
	        data: {
	            name: value, // data you need to pass to your function
	            click: True
	        }
	        success: function (data) {        
	            // success callback
	            // you can process data returned by function from views.py
	        }
	    });
	});

});