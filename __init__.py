#~ skill-finished-booting - A simple skill to know when mycroft finishes booting up.
#~ Copyright (C) 2018  zelmon64
#~ Github - https://github.com/zelmon64

#~ This program is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ This program is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with this program.  If not, see <http://www.gnu.org/licenses/>.

from mycroft import MycroftSkill
from mycroft.util.log import LOG

class FinishedBootingSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(FinishedBootingSkill, self).__init__(name="FinishedBootingSkill")
    
    def initialize(self):
        self.add_event("mycroft.skills.initialized", self.handle_boot_finished)
        LOG.debug('add event handle boot finished')
    
    def handle_boot_finished(self):
        self.speak_dialog('finished.booting')
        LOG.debug('finished booting')

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return FinishedBootingSkill()
