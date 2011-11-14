=====================
Incoming Feeds and KM
=====================

- This is *not* about import.  External resources remain external.

- UUID and docid

- internal created/modified dates vs. feed dates

- categories vs. tags

- authors matched up to internal authors?  who should be the
  resource.creator, the "system", or the moderator, or a knob?

- knobs to set the persistence (transient vs. permanent)

- do we ever try and find out what external resources disappeared or
  moved?

- do we try to provide a short __name__?  If so, what?  Using the UUID
  would, uhh, suck

- ensure there is a log showing what happened when the cron job ran,
  in case there's a problem, the creator can find out

- a knob to manually re-fetch the feed contents before the polling
  interval

- allow the feed to govern the polling interval?

- optimize for not performing work when a feed entry hasn't changed



Namespaced Custom Elements
==========================

- flag any login requirements

- map resource type into meaningful stuff, or indicate which LS group

- richer representation of body, perhaps of indexable content

