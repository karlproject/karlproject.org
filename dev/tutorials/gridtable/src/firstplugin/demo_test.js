
(function($){

    $(document).ready(function() {

	test("Widget attachment with no options", function() {

	    equals($('#test .text').css('background-color'),
                   'rgb(255, 255, 0)', 
		   'Wrong initial color');
            $('#test .text').grid({ });
	    equals($('#test .text').css('background-color'),
                   'rgb(0, 0, 255)', 
		   'Wrong initial color');

	});
    
	test("Widget attachment changes colors", function() {

	    equals($('#test .text').css('background-color'),
                   'rgb(255, 255, 0)', 
		   'Wrong initial color');
            $('#test .text').grid({
		bgColor: 'red'
            });
	    equals($('#test .text').css('background-color'),
                   'rgb(255, 0, 0)', 
		   'Wrong initial color');

	});
    
	test("Widget attachment changes colors", function() {

	    equals($('#test .text').css('background-color'),
                   'rgb(255, 255, 0)', 
		   'Wrong initial color');
            $('#test .text').grid({
		bgColor: 'red'
            });
	    equals($('#test .text').css('background-color'),
                   'rgb(255, 0, 0)', 
		   'Wrong initial color');

	});
    
    });

})(jQuery);

