import com.atlassian.jira.component.ComponentAccessor

def issuemanager=ComponentAccessor.issueManager
def attachmentmanager=ComponentAccessor.attachmentManager

def issueObject=issuemanager.getIssueObject("SUP-761")

def attachmentlist=attachmentmanager.getAttachments(issueObject)
def issuesummary=issueObject.getSummary()
print issuesummary
return [attachmentlist[0].filename,issuesummary] 
