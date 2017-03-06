
(function (root, $){

    'use strict';

    root.showLoading = function() {
        if ( $('#loading').length > 0 ) {
            $('#loading').show();
        }
    }

    root.hideLoading = function() {
        if ( $('#loading').length > 0 ) {
            $('#loading').hide();
        }
    }

    root.printError = function(data) {
        var error = '';
        for ( var field in data ) {
            if ( data[field] instanceof Object ) {
                error += root.printError(data[field]);
            } else {
                error += "<div>"
                if ( ['non_field_errors', 'event', 'attendee'].indexOf(field) < 0 ) {
                    error += "<span class=\"error-"+ field +"\">"+ field +":</span>";
                }
                error += data[field] + "</div>";
            }
        }

        return error;
    }


    root.printError2 = function(data) {
        var error = '';
        for ( var field in data ) {
            if ( data[field] instanceof Object ) {
                error += root.printError2(data[field]);
            } else {
                error += "<div>"
                if ( ['non_field_errors', 'event', 'attendee'].indexOf(field) < 0 ) {
                }
                error += data[field] + "</div>";
            }
        }

        return error;
    }


})(window, jQuery);
