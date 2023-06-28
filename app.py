import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():    
    if request.method == "POST":
        problem = request.form["problem"]
        recipe = request.form["recipe"]

        if problem:
            response = generate_problem_response(problem)
            print("Redirecting to index with problem result:", response)
            return redirect(url_for("index", problem_result=response))
        elif recipe:
            response = generate_recipe_response(recipe)
            print("Redirecting to index with recipe result:", response)
            return redirect(url_for("index", recipe_result=response))
    else:  # This is a GET request
        problem_result = request.args.get('problem_result')
        recipe_result = request.args.get('recipe_result')
    
    return render_template("index.html", problem_result=problem_result, recipe_result=recipe_result)


@app.route("/problem", methods=("GET", "POST"))
def handle_problem_form():
    problem = request.form.get("problem")
    response = generate_problem_response(problem)
    return redirect(url_for("index", problem_result=response))


@app.route("/recipe", methods=("GET", "POST"))
def handle_recipe_form():
    recipe = request.form.get("recipe")
    response = generate_recipe_response(recipe)
    return redirect(url_for("index", recipe_result=response))


def generate_problem_response(problem):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(problem),
        temperature=0.6,
        max_tokens=250,
    )
    print(response.choices[0].text)
    return response.choices[0].text


def generate_recipe_response(recipe):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(recipe),
        temperature=0.6,
        max_tokens=250,
    )
    print(response.choices[0].text)
    return response.choices[0].text

    # return "This is the recipe response for: " + recipe


def generate_prompt(problem):
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
        problem.capitalize()
    )

def generate_prompt(recipe):
    return """Give a recipe, step by step, including prep time, cooking time and instructions, given a food.

Food: Baked Beans on Toast

Recipe: Certainly! Here's a recipe for Baked Beans on Toast:

Prep Time: 5 minutes
Cooking Time: 20 minutes
Total Time: 25 minutes
Servings: 2

Ingredients:
- 1 can (15 ounces/425g) baked beans
- 2 slices of bread (white or whole wheat)
- Butter or margarine, for spreading
- Grated cheddar cheese, for topping (optional)
- Fresh parsley or chives, chopped (optional, for garnish)

Instructions:

1. Preheat your oven to 350°F (175°C).

2. Open the can of baked beans and pour them into a small saucepan. Place the saucepan over medium heat.

3. While the beans heat up, toast the slices of bread to your desired level of crispness. Spread butter or margarine on each slice.

4. Once the baked beans are heated through, remove them from the heat. If desired, you can add some grated cheddar cheese to the beans and stir until melted.

5. Place the buttered toast slices on a baking sheet or oven-safe dish.

6. Spoon the hot baked beans onto the toast, spreading them evenly.

7. If you added cheese to the beans, sprinkle some additional grated cheddar cheese on top.

8. Place the baking sheet or dish in the preheated oven and bake for about 10 minutes, or until the cheese is melted and bubbly (if using).

9. Remove from the oven and let it cool slightly. Sprinkle with chopped parsley or chives for garnish, if desired.

10. Serve the Baked Beans on Toast while still warm. Enjoy this comforting and simple dish as a quick breakfast, lunch, or even a light dinner.

Feel free to adjust the recipe according to your preferences. You can add extra toppings like sliced tomatoes, sautéed mushrooms, or a fried egg on top for added flavor and variety.

Food: Biryani
Recipe: Certainly! Here's a recipe for Bangladeshi Biryani:

Prep Time: 30 minutes
Marination Time: 1 hour (optional)
Cooking Time: 1 hour 30 minutes
Total Time: 2 hours
Servings: 6-8

Ingredients:
For the Rice:
- 3 cups Basmati rice
- Water for soaking and boiling
- 2 bay leaves
- 4-6 whole cloves
- 4-6 green cardamom pods
- 2-inch cinnamon stick
- Salt to taste

For the Chicken:
- 2 pounds (1 kg) chicken, cut into pieces
- 1 cup plain yogurt
- 2 tablespoons ginger paste
- 2 tablespoons garlic paste
- 2 teaspoons red chili powder
- 1 teaspoon turmeric powder
- Salt to taste

For the Biryani:
- 1/2 cup ghee or vegetable oil
- 2 large onions, thinly sliced
- 2 teaspoons whole cumin seeds
- 4-6 green chilies, slit lengthwise
- 1 cup mixed vegetables (carrots, peas, potatoes), parboiled (optional)
- 1/2 cup plain yogurt
- 1 teaspoon garam masala powder
- 1/2 teaspoon saffron strands, soaked in 2 tablespoons warm milk
- Fresh cilantro leaves, chopped (for garnish)
- Fresh mint leaves, chopped (for garnish)
- Fried onions (for garnish)

Instructions:

1. Wash the Basmati rice under running water until the water runs clear. Soak the rice in water for 30 minutes. Drain and set aside.

2. In a bowl, marinate the chicken with yogurt, ginger paste, garlic paste, red chili powder, turmeric powder, and salt. Let it marinate for at least 1 hour (or overnight in the refrigerator) for enhanced flavor.

3. In a large pot, bring water to a boil. Add the soaked and drained rice along with bay leaves, cloves, cardamom pods, cinnamon stick, and salt. Cook until the rice is 70-80% cooked (still slightly firm). Drain the rice and set aside.

4. In a separate large pan or Dutch oven, heat ghee or vegetable oil over medium heat. Add the sliced onions and sauté until golden brown and crispy. Remove half of the fried onions and set them aside for garnish.

5. To the remaining onions in the pan, add whole cumin seeds and green chilies. Sauté for a minute until fragrant.

6. Add the marinated chicken to the pan and cook on medium heat until the chicken is partially cooked and the spices are well combined, about 10 minutes.

7. If using, add the parboiled mixed vegetables and cook for an additional 5 minutes.

8. Add plain yogurt, garam masala powder, and salt to the pan. Mix well to coat the chicken and vegetables with the yogurt and spices.

9. Layer the partially cooked rice over the chicken mixture. Drizzle the saffron-infused milk over the rice. Sprinkle chopped cilantro and mint leaves on top.

10. Cover the pan tightly with a lid or aluminum foil. Reduce the heat to low and let the biryani cook for 30-40 minutes, allowing the flavors to meld together and the rice to finish cooking.

11. Once done, remove the pan from the heat and let it rest for 10 minutes before gently fluffing the rice with a fork.

12. Garnish the Bangladeshi Biryani with the reserved fried onions. Serve hot and enjoy the flavorful and aromatic biryani!


Food: {}
Recipe:""".format(
        recipe.capitalize()
    )
