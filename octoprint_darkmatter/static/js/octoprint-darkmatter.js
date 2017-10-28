$(function() {
    function DarkMatterPluginViewModel(parameters) {
        var self = this;

        $("body").eq(0).addClass("OctoPrintTheme-DarkMatter")
        $("#settings_dialog").eq(0).addClass("DarkMatter_Settings")

        }
		OCTOPRINT_VIEWMODELS.push([
        DarkMatterPluginViewModel,
		[]

    ]);
});
