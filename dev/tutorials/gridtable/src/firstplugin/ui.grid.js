

(function($){

    $.widget('ui.grid', {

        _init: function() {
	    var self = this;
	    this.originalColor = this.element.css('background-color');
            this.element.css('background-color', this.options.bgColor);

            this.element.click(function() {
                self.revertColor();
            });
        },

        revertColor: function() {
            this.element.css('background-color', this.originalColor);
        },

    });

    $.extend($.ui.grid, {
        version: '0.1',
        defaults: {
            bgColor: 'blue'
        }
    });

})(jQuery);