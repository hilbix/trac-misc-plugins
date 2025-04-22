
from	trac.core		import *
from	trac.perm		import IPermissionPolicy
from	trac.resource		import ResourceNotFound
from	trac.ticket.model	import Ticket

class VisibleTicketPolicy(Component):
	"""
	Grants permissions to the ticket reporter and users in CC.

	`trac.ini`:
	{{{
	[trac]
	permission_policies=VisibleTicketPolicy,DefaultWikiPolicy,DefaultTicketPolicy,DefaultPermissionPolicy,LegacyAttachmentPolicy

	[ticket-custom]
	visible = radio
	visible.label = Visibility
	visible.options = public|intern|restricted|private
	visible.value = intern
	}}}
	"""

	implements(IPermissionPolicy)

	allowed_actions = ('TICKET_VIEW', 'TICKET_APPEND', 'TICKET_EDIT_DESCRIPTION', 'TICKET_EDIT_CC')

	def check_permission(self, action, username, resource, perm):
		self.log.debug('VisibleTicketPolicy.check_permission(%s,%s,%r,%r)', action, username, resource, perm)
		if action not in self.allowed_actions:			return

		if resource is None:					return
		if resource.realm != 'ticket':				return
		if resource.id is None:					return
		try:
			ticket = Ticket(self.env, resource.id)
		except ResourceNotFound:
			self.log.info('VisibleTicketPolicy.check_permission: not found %r', resource.id)
			return

		self.log.debug('VisibleTicketPolicy.check_permission %s: user=%s reporter=%s',  username, ticket['user'], ticket['reporter'])

		if ticket['user'] == username:				return True
		if ticket['reporter'] == username:			return True
		if 'TRAC_ADMIN' in perm:				return True

		pub	= ticket['visible'] == 'public'
		restrict= ticket['visible'] == 'restricted'
		private	= ticket['visible'] == 'private'

		cc	= username in ticket['cc'].split(', ') 

		self.log.debug('VisibleTicketPolicy.check_permission: pub=%s restrict=%s private=%s cc=%s',  pub, restrict, private, cc)

		if action == 'TICKET_VIEW':
			if pub or cc:	return True
		if action == 'TICKET_APPEND':
			if restrict:	return		# cc can only view
			if cc:		return True

		if private:	return False	# overwrites TICKET_VIEW permission

		# return None such that further modules check the perm

