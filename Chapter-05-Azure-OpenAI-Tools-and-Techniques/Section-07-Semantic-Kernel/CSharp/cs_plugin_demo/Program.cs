// See https://aka.ms/new-console-template for more information
//using Microsoft.Extensions.Logging;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Planning;
using Microsoft.SemanticKernel.Functions.OpenAPI.Extensions;
using Microsoft.SemanticKernel.Planners;

// Create a kernel here...
var kernel_builder = new KernelBuilder().WithAzureChatCompletionService(
    "gpt-35-turbo-16k",                   // Azure OpenAI *Deployment Name*
    "YOUR AZURE OPENAI ENDPOINT",    // Azure OpenAI *Endpoint*
    "YOUR AZURE OPENAI API KEY",          // Azure OpenAI *Key*
    serviceId: "Azure_curie"                // alias used in the prompt templates' config.json
);

IKernel kernel = kernel_builder.Build();

// Add the math plugin using the plugin manifest URL
const string pluginManifestUrl = "http://localhost:8080/.well-known/ai-plugin.json";
var EventApiForGPTPlugin = await kernel.ImportPluginFunctionsAsync("EventApiForGPTPlugin", new Uri(pluginManifestUrl));

// Create a stepwise planner and invoke it
var planner = new StepwisePlanner(kernel);
var ask = "Please show the current plan";
var plan = planner.CreatePlan(ask);
var result = await kernel.RunAsync(plan);

// Print the results
Console.WriteLine(result);