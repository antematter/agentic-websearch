from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from websearch.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

@CrewBase
class Websearch:
	"""Websearch crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def web_searcher(self) -> Agent:
		return Agent(
			config=self.agents_config['web_searcher'],
			tools=[SerperDevTool()], 
			verbose=True
		)

	@agent
	def summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['summarizer'],
			tools=[ScrapeWebsiteTool()],
			verbose=True
		)
	
	@agent
	def answer_gen(self) -> Agent:
		return Agent(
			config=self.agents_config['answer_gen'],
			verbose=True
		)

	@task
	def web_searcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['web_searcher_task'],
		)

	@task
	def summarizer_task(self) -> Task:
		return Task(
			config=self.tasks_config['summarizer_task'],
			# output_file='report.md'
		)
	
	@task
	def answer_gen_task(self) -> Task:
		return Task(
			config=self.tasks_config['answer_gen_task'],
			# output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Websearch crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
