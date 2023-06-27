import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=500,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Give a high level plan for the desired outcome

Outcome: I want to migrate to the cloud
High Level Plan: Define your objectives: Determine why you want to migrate to the cloud. Identify the specific goals you want to achieve, such as cost savings, scalability, improved performance, or enhanced security.

Assess your current environment: Conduct a thorough assessment of your existing infrastructure, applications, and data. Understand the dependencies, interconnections, and potential challenges that may arise during the migration process.

Choose the right cloud provider: Evaluate different cloud providers (such as Amazon Web Services, Microsoft Azure, or Google Cloud) based on your requirements, budget, and the services they offer. Consider factors like reliability, security, performance, and support.

Plan your migration strategy: Develop a detailed migration plan that includes a timeline, resource allocation, and specific tasks. Decide on the migration approach, whether it's a lift-and-shift, re-platforming, or a complete application redesign.

Ensure data security: Prioritize data security during the migration. Implement encryption, access controls, and other security measures to protect your sensitive information. Consider compliance requirements specific to your industry.

Migrate in phases: Divide the migration process into manageable phases or iterations. Start with non-critical applications or low-impact workloads to gain experience and confidence. Gradually move more critical systems as you learn and refine your approach.

Optimize and re-architect: Use the migration as an opportunity to optimize your infrastructure and applications. Consider cloud-native architectures, auto-scaling, and serverless computing to fully leverage the benefits of the cloud.

Test and validate: Test your migrated applications thoroughly to ensure they function correctly in the cloud environment. Conduct performance testing, load testing, and security assessments to validate the reliability and scalability of your new setup.

Train and educate your team: Provide training and education to your IT team to familiarize them with the cloud environment and associated tools. This will enable them to effectively manage and troubleshoot any issues that may arise.

Monitor and optimize: Once your migration is complete, establish a robust monitoring and optimization strategy. Continuously monitor your cloud resources, performance metrics, and cost utilization. Optimize your deployments to achieve cost savings and improve performance.

Outcome: I want to optimise to my cloud deployment
High Level Plan: Optimizing your cloud deployment can help you achieve cost savings, improve performance, and enhance the overall efficiency of your cloud infrastructure. Here are some strategies you can consider:

1. Right-size your resources: Regularly analyze the resource utilization of your cloud instances and services. Adjust the size of your virtual machines, storage, and database instances to match the actual workload requirements. Avoid over-provisioning and under-utilization to optimize costs.

2. Utilize auto-scaling: Leverage auto-scaling capabilities provided by your cloud provider to automatically adjust resources based on demand. Set up scaling policies to add or remove instances dynamically, ensuring you have enough resources during peak periods while avoiding unnecessary costs during periods of low demand.

3. Use reserved instances or savings plans: Take advantage of reserved instances or savings plans offered by cloud providers. These options provide discounted pricing for committed usage over a period of time, allowing you to save significantly on your cloud costs.

4. Optimize storage costs: Evaluate your storage needs and choose the appropriate storage types and tiers for your data. Consider utilizing object storage, archival storage, or tiered storage options based on the frequency of access and performance requirements. Enable data lifecycle management to automatically move data to cost-effective storage tiers.

5. Monitor and optimize network traffic: Monitor your network traffic and identify any inefficiencies or bottlenecks. Use content delivery networks (CDNs) to cache and deliver content closer to end-users, reducing latency and bandwidth costs. Implement traffic routing and load balancing to optimize network performance.

6. Containerize applications: Containerization using technologies like Docker and Kubernetes can improve resource utilization and deployment efficiency. Containerized applications can scale easily, utilize resources efficiently, and enable rapid deployment and updates.

7. Implement serverless computing: Consider leveraging serverless computing platforms such as AWS Lambda or Azure Functions. Serverless architectures allow you to execute code without managing servers, providing automatic scaling and cost optimization by charging only for actual usage.

8. Continuous optimization and cost monitoring: Regularly review your cloud infrastructure, usage patterns, and cost reports. Use cloud provider tools or third-party services to gain insights into your cloud spend and identify areas for optimization. Set up alerts and notifications to detect any unusual or unexpected usage patterns.

9. Adopt cloud governance and cost management practices: Implement cloud governance policies and controls to manage resource allocation, permissions, and spending across your organization. Establish budgets, tagging strategies, and access controls to enforce cost management practices and ensure accountability.

10. Engage with cloud provider support and resources: Take advantage of the support and resources provided by your cloud provider. Attend webinars, workshops, and training sessions to stay updated on new services and optimization techniques. Consult with their experts to get guidance specific to your deployment.

Remember that optimization is an ongoing process. Regularly assess and fine-tune your cloud deployment to align with your evolving needs and to take advantage of new cost-saving features and services offered by your cloud provider.


Outcome: {}
High Level Plan:""".format(
        animal.capitalize()
    )
