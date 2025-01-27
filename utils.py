def register_tools(assistant, executor, tools):
    for tool in tools:
        assistant.register_for_llm(name=tool['name'], description=tool['description'])(tool['func'])
        executor.register_for_execution(name=tool['name'])(tool['func'])
