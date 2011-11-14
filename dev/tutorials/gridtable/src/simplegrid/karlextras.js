
new (function() {                  // BEGIN CLOSURE extras

var t = this;

$.widget('ui.karlgrid', $.extend({}, $.ui.grid.prototype, {

    _generateColumns: function() {

        this.columnsContainer = $('<tr class="ui-grid-columns"><td><div class="ui-grid-columns-constrainer"><table cellpadding="0" cellspacing="0"><tbody><tr class="ui-grid-header ui-grid-inner"></tr></tbody></table></div></td></tr>')
            .appendTo(this.grid).find('table tbody tr');

        $('.ui-grid-columns-constrainer', this.grid).css({
            width: this.options.width,
            overflow: 'hidden'
        });
        
        // columns will have borders collapsed
        $('table', this.grid).css({
            'border-collapse': 'collapse'
        });

        // XXX Do _not_ make it sortable.
        //this.columnsContainer.gridSortable({ instance: this });
        
    },

    _syncColumnWidth: function() {
        var self = this;

        // calculate desired widths
        var column_widths = [];
        var totalWidth = 0;
        $('td', this.columnsContainer).each(function() {
            var width = $(this).outerWidth();
            column_widths.push(width);
            totalWidth += width;
        });
        
        // set width on all cells
        // XXX This would probably work bad with infinite scrolling!
        $('> tr', this.content).each(function() {
            $('> td', this).each(function(i) {
                var elem = $(this);
                var width = column_widths[i];
                // Take offset into consideration
                var offset = elem.outerWidth() - elem.width();
                if (i==0) {
                    // Since we have no bordercollapse in the column part:
                    // increase first field's width with the left border
                    offset -= self.leftBorder; 
                }
                width -= offset;
                // adjust cell width
                elem
                    // overflow is essential for column width
                    .css('overflow', 'hidden')
                    .width(width);
            });

        });

        // set the width of the whole table
        this.content.parent()     // this.content is the <tbody>, parent is the <table>.
            .width(totalWidth)
            //.css('overflow', 'hidden')
            // table-layout is essential for column width
            .css('table-layout', 'fixed');

    },

    _addColumns: function(columns) {

        this.columns = columns;
        //// XXX XXX there is no placeholder column now
        //var totalWidth = 25;
        var totalWidth = 0;
        this.columns_by_id = {};
        
        // Use sort column and direction as set by _onClick handler,
        // allow to provide initial defaults by options.
        var sortColumn = this.sortColumn || this.options.sortColumn;
        var sortDirection = this.sortDirection || this.options.sortDirection;

        for (var i=0; i < columns.length; i++) {
            var column_meta = columns[i];

            var sortDirectionClass = '';
            // Do we have a sorting direction?
            if (sortColumn == column_meta.id) {
                sortDirectionClass = ' ui-icon ' + (sortDirection == 'asc' ? 'ui-icon-carat-1-s' : 'ui-icon-carat-1-n');
            }

            var column = $('<td class="ui-grid-column-header ui-state-default">' +
                           '  <div style="position: relative;">' + // inner div is needed for relativizing position
                           '    <a href="#">' +
                           '      <span class="ui-grid-column-header-text">' + column_meta.label + '</span>' +
                           '    </a>' +
                           '    <span class="ui-grid-visual-sorting-indicator' + sortDirectionClass + '"></span>' +
                           '  </div>' +
                           '</td>')
                .data('grid-column-header', column_meta)
                .appendTo(this.columnsContainer);

            var offset = column.outerWidth() - column.width();
            if (i==0) {
                // the first column gets the left offset
                // subscribed from width as well
                // this is needed to compensate for left column border
                //this.leftBorder = column[0].offsetLeft;
                if (jQuery.browser.msie) {
                    this.leftBorder = 0;
                } else {
                    // FF, Safari
                    // XXX for now we suppose a (table) border of 1
                    this.leftBorder = 1;
                }
                offset += this.leftBorder;
            }
            column.width(column_meta.width - offset);

            totalWidth += column_meta.width;
            
            // XXX Do not make the columns resizable.
            //column.gridResizable();
        };
        
        //This column is the last and only used to serve as placeholder for a non-existant scrollbar
        // XXX XXX temporary disabled, as currently we don't use features it allows,
        // and it causes a layout artifact on FF.
        //$('<td class="ui-grid-column-header ui-state-default"><div></div></td>').width(25).appendTo(this.columnsContainer);
        
        //Update the total width of the wrapper of the column headers
        var header_table = this.columnsContainer.parent().parent();
        header_table.width(totalWidth);

        // Send event that columns are setup
        this.element.trigger('karlgrid_columns_set');

    },

    _handleClick: function(event) {

        var el = $(event.target);

        // Click on column header toggles sorting
        if (el.is('.ui-grid-column-header, .ui-grid-column-header *')) {
            var header = el.hasClass('ui-grid-column-header') ? el : el.parents('.ui-grid-column-header');
            var data = header.data('grid-column-header');
            this.sortDirection = this.sortDirection == 'desc' ? 'asc' : 'desc';
            this.sortColumn = data.id;
            this._update ({columns: false, refresh: true});
        }
        
        // Handle click on pagination buttons
        if (el.is('.ui-grid-pagination a, .ui-grid-pagination a *')) {
            var current= Math.floor((this.offset + this.options.limit - 1) / this.options.limit) + 1;
            if (el.hasClass('ui-icon-circle-arrow-w') || el.find('.ui-icon-circle-arrow-w').length > 0) current --;
            if (el.hasClass('ui-icon-circle-arrow-e') || el.find('.ui-icon-circle-arrow-e').length > 0) current ++;
            if (! isNaN(parseInt(event.target.innerHTML, 10))) current = parseInt(event.target.innerHTML, 10);
            
            this.offset = (current - 1) * this.options.limit;
            this._update();
        }
        
        return false;

    },


    _makeRowsSelectable: function() {
        
        var table = this.content.parent().parent();
        table.bind('mousedown', function(event) {
            var filter = 'tr';
            var item;
            $(event.target).parents().andSelf().each(function() {
                if ($('tr', table).index(this) != -1) item = this;
            });

            if (!item)
                return;

            // follow the link in it
            var links = $('a', item);
            if (links.length > 0) {
                window.location = links[0].href;
            }

            event.preventDefault();
        });
        
    },

    _addRow: function(item, dontAdd) {

        var row = $.ui.grid.prototype._addRow.call(this, item, dontAdd);

        // Calculate the oddity of the newly added row. We do the
        // following check after the row has already been added.
        var oddity = (this.content.find('tr').length % 2 == 1)

        // Add class based on oddity and options
        if (oddity && this.options.oddRowClass) {
            row.addClass(this.options.oddRowClass);
        }

        if (! oddity && this.options.evenRowClass) {
            row.addClass(this.options.evenRowClass);
        }

        return row;

    },

    _generateFooter: function() {
        this.footer = $('<tr class="ui-grid-footer ui-widget-header"><td>'+
        '<span class="ui-grid-footer-text ui-grid-limits"></span>'+
        '</td></tr>').appendTo(this.grid).find('td');
    },

    _generatePagination: function(response) {
        this.pagination = $('<span class="ui-grid-pagination clearafter"></span>').appendTo(this.footer);
        this.footerResultsBox = $('.ui-grid-limits, .ui-grid-no-limits', this.footer);
        this._updatePagination(response);
    },

    /* XXX need to overwrite this for not showing
     * pagination if there are 0 or 1 pages */
    _updatePagination: function(response) {
        
        var pages = Math.floor((response.totalRecords + this.options.limit - 1) / this.options.limit),
            current= Math.floor((this.offset + this.options.limit - 1) / this.options.limit) + 1,
            displayed = [];

        this.pagination.empty();
        
        if (pages <= 1) {
            // Deactivate the Results: box
            // This means that if it does not have the ui-grid-limits
            // class, the updater won't update the Results: infoline on it
            this.footerResultsBox
                .removeClass('ui-grid-limits')
                .addClass('ui-grid-no-limits')
                .html('');
            return;
        }

        // Activate the Results: box
        this.footerResultsBox
            .removeClass('ui-grid-no-limits')
            .addClass('ui-grid-limits');

        for (var i=current-1; i > 0 && i > current-3; i--) {
            this.pagination.prepend('<a href="#" class="ui-state-default">'+i+'</a>');
            displayed.push(i);
        };
        
        for (var i=current; i < pages+1 && i < current+3; i++) {
            this.pagination.append(i==current? '<span class="ui-state-active">'+i+'</span>' :
                    '<a href="#" class="ui-state-default">'+i+'</a>' );
            displayed.push(i);
        };


        if(pages > 1 && $.inArray(2, displayed) == -1) //Show front dots if the '2' is not already displayed and there are more pages than 1
            // XXX XXX
            this.pagination.prepend('<span class="ui-grid-pagination-dots">...</span>');
        
        if($.inArray(1, displayed) == -1) //Show the '1' if it's not already shown
            this.pagination.prepend('<a href="#" class="ui-state-default">1</a>');

        if($.inArray(pages-1, displayed) == -1) //Show the dots between the current elipse and the last if the one before last is not shown
            // XXX XXX
            this.pagination.append('<span class="ui-grid-pagination-dots">...</span>');
        
        if($.inArray(pages, displayed) == -1) //Show the last if it's not already shown
            this.pagination.append('<a href="#" class="ui-state-default">'+pages+'</a>');
            
        this.pagination.prepend(current-1 > 0 ?
                '<a href="#" class="ui-state-default ui-grid-pagination-icon"><div class="ui-icon ui-icon-circle-arrow-w">Prev</div></a>' :
                '<span class="ui-state-default ui-state-disabled ui-grid-pagination-icon"><div class="ui-icon ui-icon-circle-arrow-w">Prev</div></span>');
        this.pagination.append(current+1 > pages ?
                '<span href="#" class="ui-state-default ui-state-disabled ui-grid-pagination-icon"><div class="ui-icon ui-icon-circle-arrow-e">Next</div></span>' :
                '<a href="#" class="ui-state-default ui-grid-pagination-icon"><div class="ui-icon ui-icon-circle-arrow-e">Next</div></a>');

        this.pagination.find('a.ui-state-default')
            .hover(
                function() {
                    $(this).addClass('ui-state-hover');
                },
                function() {
                    $(this).removeClass('ui-state-hover');
                }
            );

    },

    _extendFetchOptions: function(fetchOptions) {
        return $.extend({}, fetchOptions, {
            limit: this.options.limit,
            start: (! (fetchOptions && fetchOptions.refresh) && this.offset) || 0,
            refresh: (fetchOptions && fetchOptions.refresh) || (fetchOptions && fetchOptions.columns)
        })
    },

    /* XXX need to overwrite this to be able to customize
     * behaviour like displaying Results data.  */
    _update: function(o) {
        var self = this;

        var fetchOptions = $.extend({}, this._extendFetchOptions(fetchOptions), {
        // XXX Is this needed?
        //    fill: null
        });
        
        if (fetchOptions.refresh) {
            fetchOptions.start = this.infiniteScrolling ? 0 : (this.offset || 0);
        }
        //Somehow the keys for these must stay undefined no matter what
        if(this.sortColumn) fetchOptions.sortColumn = this.sortColumn;
        if(this.sortDirection) fetchOptions.sortDirection = this.sortDirection;

        //Do the ajax call
        this.gridmodel.fetch(fetchOptions, function(state) {
            self._doUpdate(state, o);
        });

    },

    _initialUpdate: function() {
        var initialState = this.options.initialState;
        if (initialState) {
            // Initial state: use it to load content
            // Need to convert each record from a flat list to a keyed dict
            initialState = $.ui.grid.model.defaults.parse(initialState);
            // load them to the table
            this._doUpdate(initialState, {columns: true});
        } else {
            // Query the content from the server
            this._update({columns: true});
        }
    },

    /* XXX Added for demo */
    addRows: function(rows) {
        var self = this;
        // Need to convert each record from a flat list to a keyed dict
        //var state = $.ui.grid.model.defaults.parse({records: rows});
        var records = [];
        $.each(rows, function() {
            var record = this;
            var result = {};
            $.each(self.columns, function(index) {
                result[this.id] = record[index];
            })
            records.push(result);
        });
        // load them to the table
        // XXX XXX XXX
        this._doUpdate({records: records}, {columns: false});
    },

    _doUpdate: function(state, o) {
        var self = this;

        //Generate or update pagination
        if (this.options.pagination && ! this.pagination) {
            this._generatePagination(state);
        } else if (this.options.pagination && this.pagination) {
            this._updatePagination(state);
        }

        var self = this;
        var fetchOptions = this._extendFetchOptions(o);

        //Empty the content if we either use pagination or we have to restart infinite scrolling
        if (!this.infiniteScrolling || fetchOptions.refresh)
            this.content.empty();

        //Empty the columns
        if (fetchOptions.refresh) {
            this.columnsContainer.empty();
            this._addColumns(state.columns);
        }

        //If infiniteScrolling is used and there's no full refresh, fill rows
        if(this.infiniteScrolling && ! fetchOptions.refresh) {

            var data = [];
            for (var i=0; i < state.records.length; i++) {
                data.push(this._addRow(state.records[i]));
            };

            o.fill({
                chunk: o.chunk,
                data: data
            });

        } else { //otherwise, simply append the rows to the now emptied list

            for (var i=0; i < state.records.length; i++) {
                this._addRow(state.records[i]);
            };

            this._syncColumnWidth();
                
            //If we're using infinite scrolling, we have to restart it
            if(this.infiniteScrolling) {
                this.contentDiv.infiniteScrolling('restart');
            }

        }

        //Initiate infinite scrolling if we don't use pagination and total records exceed the displayed records
        if(!this.infiniteScrolling && !this.options.pagination && fetchOptions.limit < state.totalRecords) {
                
            this.infiniteScrolling = true;
            this.contentDiv.infiniteScrolling({
                total: self.options.allocateRows ? state.totalRecords : false,
                chunk: self.options.chunk,
                scroll: function(e, ui) {
                    self.offset = ui.start;
                    self._update({ fill: ui.fill, chunk: ui.chunk });
                },
                update: function(e, ui) {
                    $('.ui-grid-limits', self.footer).html('Result ' + ui.firstItem + '-' + ui.lastItem + (ui.total ? ' of '+ui.total : ''));
                }
            });
                
        }

        if(!this.infiniteScrolling)
            $('.ui-grid-limits', this.footer).html('Result ' + fetchOptions.start + '-' + (fetchOptions.start + fetchOptions.limit) + ' of ' + state.totalRecords);

    }
 
}));


$.extend($.ui.karlgrid, {
    defaults: {
        width: 500,
        height: 300,

        limit: false,
        pagination: true,
        allocateRows: true, //Only used for infinite scrolling
        chunk: 20, //Only used for infinite scrolling

        footer: true,
        toolbar: false,

        multipleSelection: true,

        evenRowClass: 'even',
        oddRowClass: 'odd',

        sortColumn: '',
        sortDirection: '',

        initialState: null
    }
});

})();                   // END CLOSURE extras

