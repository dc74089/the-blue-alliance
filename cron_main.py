#!/usr/bin/env python

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from controllers.datafeed_controller import TbaVideosGet
from controllers.datafeed_controller import UsfirstEventGetEnqueue, UsfirstEventGet, UsfirstEventsInstantiate
from controllers.datafeed_controller import UsfirstMatchesGetEnqueue, UsfirstMatchesGet
from controllers.datafeed_controller import UsfirstTeamGetEnqueue, UsfirstTeamGet, UsfirstTeamsInstantiate
from controllers.datafeed_controller import FlushTeams, FlushMatches, FlushEvents

from controllers.cron_controller import EventTeamUpdater

def main():
    application = webapp.WSGIApplication([('/tasks/eventteam_update/(.*)', EventTeamUpdater),
                                          ('/tasks/tba_videos_get/(.*)', TbaVideosGet),
                                          ('/tasks/usfirst_event_get_enqueue', UsfirstEventGetEnqueue),
                                          ('/tasks/usfirst_event_get/(.*)', UsfirstEventGet),
                                          ('/tasks/usfirst_events_instantiate', UsfirstEventsInstantiate),
                                          ('/tasks/usfirst_matches_get_enqueue', UsfirstMatchesGetEnqueue),
                                          ('/tasks/usfirst_matches_get/(.*)', UsfirstMatchesGet),
                                          ('/tasks/usfirst_team_get_enqueue', UsfirstTeamGetEnqueue),
                                          ('/tasks/usfirst_team_get/(.*)', UsfirstTeamGet),
                                          ('/tasks/usfirst_teams_instantiate', UsfirstTeamsInstantiate),
                                          ('/tasks/flush/events', FlushEvents), # Danger!
                                          ('/tasks/flush/matches', FlushMatches), # Danger!
                                          ('/tasks/flush/teams', FlushTeams), # Danger!
                                          ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
