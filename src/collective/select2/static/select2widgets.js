/*global window, jQuery, document */
(function ($) {
    "use strict";
    if ((typeof window.select2widgets) === 'undefined') {
        window.select2widgets = {};
    }

    var select2widgets = window.select2widgets;

    select2widgets.select2InputWidget = function (trigger, settings) {
        var self = this;
        $.extend(this, settings);
        self.trigger = $(trigger);
        self.init();
    };

    select2widgets.select2InputWidget.prototype = {
        init: function () {
            var self = this;
            self.trigger.select2({
                minimumInputLength: 3,
                width: 'element',
                initSelection : function (element, callback) {
                    var data = [],
                        initialValues = self.trigger.data('select2Initialvalues');

                    $(element.val().split(",")).each(function () {
                        data.push({id: this, text: initialValues[this]});
                    });
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
                multiple: true
            });
        }
    };

    $.fn.extend({
        select2InputWidget: function (options) {
            return this.each(function () {

                var settings = $.extend(true, {}, options),
                    $this = $(this),
                    data = $this.data('select'),
                    widget;

                // If the plugin hasn't been initialized yet
                if (!data) {
                    widget = new select2widgets.select2InputWidget(this, settings);

                    $(this).data('select2InputWidget', {
                        widget: widget
                    });
                }
            });
        }
    });

    $(document).ready(function() {
        $('.select2-widget').select2InputWidget();
    });

}(jQuery));

