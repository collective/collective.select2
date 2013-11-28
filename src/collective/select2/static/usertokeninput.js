/*global window, jQuery, document, alert */
(function ($) {
    "use strict";
    if ((typeof window.usertokeninput) === 'undefined') {
        window.usertokeninput = {};
    }

    var usertokeninput = window.usertokeninput;

    usertokeninput.userTokenInput = function (trigger, settings) {
        var self = this;
        $.extend(this, settings);
        self.trigger = $(trigger);
        self.init();
    };

    usertokeninput.userTokenInput.prototype = {
        init: function () {
            var self = this;
            self.trigger.select2({
                minimumInputLength: 3,
                width: 'element',
                initSelection : function (element, callback) {
                    var data = [],
                        initialValues = self.trigger.data('usertoken-initialvalues');

                    $(element.val().split(",")).each(function () {
                        data.push({id: this, text: initialValues[this]});
                    });
                    callback(data);
                },

                ajax: {
                    url: self.trigger.data('usertoken-url'),
                    dataType: 'json',
                    data: function (term, page) {
                        return {
                            term: term,
                            strict: true
                        };
                    },
                    results: function (data, page) {
                        return {
                            results: data
                        };
                    }
                },
                multiple: true
            });
        }
    };

    $.fn.extend({
        userTokenInput: function (options) {
            return this.each(function () {

                var settings = $.extend(true, {}, options),
                    $this = $(this),
                    data = $this.data('usertokeninput'),
                    widget;

                // If the plugin hasn't been initialized yet
                if (!data) {
                    widget = new usertokeninput.userTokenInput(this, settings);

                    $(this).data('usertokeninput', {
                        target: $this,
                        widget: widget
                    });
                }
            });
        }
    });

    $(document).ready(function() {
        $('.usertokeninput-widget').userTokenInput();
    });

}(jQuery));

