
(function($){


$.widget('ui.multistatusbox', {
    
    _init: function() {
        // add container class to container
        this.element.addClass(this.options.clsContainer);
    },

    /*
     * Public methods
     **/

    /* Clear all messages */
    clear: function() {
        this.element.empty();
    },

    /* Append a message */
    append: function(message) {
        // Append the item
        var item = $('<div class="ui-multistatusbox-item ui-helper-clearfix"></div>');
        // Add item classes to the item
        item.addClass(this.options.clsItem);
        // Create message and (if needed) a close button
        item.append($('<div class="ui-multistatusbox-message"></div>').append(message));
        if (this.options.hasCloseButton) {
            item.append($('<a href="#" class="ui-multistatusbox-closebutton">' + 
                          '<span class="ui-icon ui-icon-closethick">X</span></a>')
                        .hover(
                            function(e) { $(this).addClass('ui-state-hover'); },
                            function(e) { $(this).removeClass('ui-state-hover'); }
                        )
                        .click(function(e) {
                            item.remove();    
                            e.preventDefault();
                        })
            );
        }
        this.element.append(item);
    },


    /*
     * Private methods
     **/


});

$.extend($.ui.multistatusbox, {
    defaults: {
        clsContainer: 'ui-widget',
        clsItem: 'ui-state-highlight ui-corner-all',
        hasCloseButton: true
    }
});


})(jQuery);

