data = """
2014-08-01 02:34:08,054 INFO  [u2.client.agents] com.mcafee.tsw.agent.AgentManager.run Shutting down the agent.
2014-08-01 02:37:06,047 INFO  [u2.client.agents] com.mcafee.tsw.agent.AgentManager.<init> Adding Provider Class to manager. class=com.mcafee.tsw.agent.provider.PublishPrevalenceProvider
2014-08-01 02:37:06,189 INFO  [u2.client.agents] com.mcafee.tsw.agent.AgentManager.getAgentLock Getting agent lock for agent=Publish
2014-08-01 02:37:06,963 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishXl Number of URLs Inserted into XL: 5
2014-08-01 02:37:06,967 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishXl Number of Parent Domains Inserted into XL: 0
2014-08-01 02:37:06,970 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishXl Number of URLs removed from XL: 0
2014-08-01 02:37:06,997 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishXl Total number of XL Updates: 25
2014-08-01 02:37:07,012 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishTs Number of URLs ensured to be publish in TS: 34
2014-08-01 02:37:07,041 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishTs Number of prevalence URLs to be published in TS: 0
2014-08-01 02:37:07,069 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishTs Number of parents URLs to be published in TS: 0
2014-08-01 02:37:07,105 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishTs Number of is_generated IPs removed from TS: 0
2014-08-01 02:37:07,166 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishTs Removed URLs from TS: timestamp = 2014-07-02, categories = ms, count = 0
2014-08-01 02:37:07,169 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishTs Total Number of URLs Removed from TS: 0
2014-08-01 02:37:07,169 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.publishTs Total Number of TS Updates: 34
2014-08-01 02:37:07,170 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.syncPrevalenceWithBuildTable Starting sync of prevalence table with the build table.
2014-08-01 02:37:07,190 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.syncPrevalenceWithBuildTable Deleted from prevalence table deleted_clhash=0
2014-08-01 02:37:07,206 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.syncPrevalenceWithBuildTable Inserted into prevalence inserted_clhash=0
2014-08-01 02:37:07,207 INFO  [u2.client.agents] com.mcafee.tsw.api.PublishPrevalence.syncPrevalenceWithBuildTable Finish sync of prevalence table with the build table.
2014-08-01 02:37:36,197 INFO  [u2.client.agents] com.mcafee.tsw.agent.AgentManager.run Shutting down the agent."""

# print(data)
print(len(data))
print(type(data))

import re
v = re.search(r'(Number of URLs Inserted into XL: )(\d+)', data)
print(v)
print(type(v))
print(v.group())
print(v.group(0))
print(v.group(1))
print(v.group(2))
