# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class DarkMatterPlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			css=["css/darkmatter.css",
			"css/bootstrap-modal.css",
			"css/overrides.css",
			"css/overrides-icons.css"],
			js=["js/octoprint-darkmatter.js"],
			img=["img/noise.png",
			"img/stripes.svg",
			"img/extruder.svg"],
			fonts=["fonts/DIN.woff"]
	)


	def get_update_information(self):
		return dict(
			darkmatter=dict(
				displayName="DarkMatter Theme",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="apollo-ng",
				repo="Octoprint-DarkMatter",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/apollo-ng/Octoprint-DarkMatter/archive/{target_version}.zip"
		)
	)

__plugin_name__ = "DarkMatter Theme"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = __plugin_implementation__ = DarkMatterPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
