# encoding: utf-8

import gvsig

from org.gvsig.andami import PluginsLocator
from org.gvsig.app import ApplicationLocator
from snappingTool import QuickSnappingToolExtension

from java.io import File
from org.gvsig.tools.swing.api import ToolsSwingLocator

from gvsig import getResource
from org.gvsig.tools import ToolsLocator

def selfRegister():
  application = ApplicationLocator.getManager()
  i18n = ToolsLocator.getI18nManager()

  icon_show = File(gvsig.getResource(__file__,"images", "snap16x16.png")).toURI().toURL()

  iconTheme = ToolsSwingLocator.getIconThemeManager().getCurrent()
  iconTheme.registerDefault("scripting.quick-snapping-tool", "action", "tools-quick-snapping-tool", None, icon_show)
  
  extension = QuickSnappingToolExtension()

  actionManager = PluginsLocator.getActionInfoManager()
  action_show = actionManager.createAction(
    extension, 
    "tools-quick-snapping-tool", # Action name
    i18n.getTranslation("_Quick_Snapping_Tool"), # Text
    "show", # Action command
    "tools-quick-snapping-tool", # Icon name
    None, # Accelerator
    3000999999, # Position 
    "Quick Snapping Tool" # Tooltip
  )
  action_show = actionManager.registerAction(action_show)
  application.addTool(action_show, i18n.getTranslation("_Quick_Snapping_Tool"))

def selfRegisterI18n():
  i18nManager = ToolsLocator.getI18nManager()
  i18nManager.addResourceFamily("text",File(getResource(__file__,"i18n")))
  
def main(*args):
  selfRegisterI18n()
  selfRegister()
