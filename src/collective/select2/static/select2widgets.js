/*global window, jQuery, document */
(function ($) {
    "use strict";
    if ((typeof window.select2widgets) === 'undefined') {
        window.select2widgets = {};
    }

    var select2widgets = window.select2widgets;

    select2widgets.select2Widget = function (trigger, settings) {
        var self = this;
        $.extend(this, settings);
        self.trigger = $(trigger);
        self.init();
    };

    select2widgets.select2Widget.prototype = {
        init: function () {
            var self = this,
                multiple = self.multiple ? true : false;
            self.trigger.select2({
                minimumInputLength: 3,
                width: 'element',
                initSelection : function (element, callback) {
                    var data = [],
                        initialValues = self.trigger.data('select2Initialvalues');

                    $(element.val().split(",")).each(function () {
                        if (this)
                            data.push({id: this, text: initialValues[this]});
                    });

                    if (data && (! multiple)) {
                        data = data[0];
                    }
                    callback(data);
                },

                ajax: {
                    url: self.trigger.data('select2Url'),
                    dataType: 'json',
                    data: function (term, page) {
                        return {
                            term: term,
                            add_terms: true
                        };
                    },
                    results: function (data, page) {
                        return {
                            results: data
                        };
                    }
                },
                multiple: multiple
            });
        }
    };

    $.fn.extend({
        select2Widget: function (options) {
            return this.each(function () {

                var settings = $.extend(true, {}, options),
                    $this = $(this),
                    data = $this.data('select'),
                    widget;

                // If the plugin hasn't been initialized yet
                if (!data) {
                    widget = new select2widgets.select2Widget(this, settings);

                    $(this).data('select2Widget', {
                        widget: widget
                    });
                }
            });
        }
    });

    $(document).ready(function() {
        $('.select2-multi-widget').select2Widget({
            multiple: true
        });

        $('.select2-widget').select2Widget({
            multiple: false
        });

    });

}(jQuery));

