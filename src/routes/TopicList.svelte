<script lang="ts">
	import { questionPath } from "$lib/const";
	import { createEventDispatcher } from "svelte";

	// For storing topics and selected topics
	let topicDict: { [id: string]: Number } = {};
	export let selectedTopics: Array<String> = [];

	// For sending event on topic load
	const dispatch = createEventDispatcher();

	// Async load topics
	async function loadTopicsList() {
		const res = await fetch(questionPath + "/_topics.json");
		const resp = await res.text();

		if (res.ok) {
			topicDict = JSON.parse(resp);

			return true;
		} else {
			throw new Error(resp);
		}
	}

	// Execute load topics
	let topicsPromise = loadTopicsList();

	// Function for toggling a topic selected/deselected
	function toggleTopic(topic: String) {
		if (selectedTopics.indexOf(topic) > -1) {
			selectedTopics.splice(selectedTopics.indexOf(topic), 1);
			selectedTopics = selectedTopics;
		} else {
			selectedTopics = [...selectedTopics, topic];
		}
	}

	// Notify user of how many potential questions have been selected
	$: {
		selectedTopics;
		{
			let sum = 0;
			selectedTopics.forEach((key) => {
				sum += topicDict[key as string] as number; // Again, this is stupid
			});
			dispatch("maxQuestionsChanged", {
				numQuestions: sum,
			});
		}
	}
</script>

<div class="box">
	<h2 class="is-size-3 is-underlined">Topics</h2>

	{#await topicsPromise}
		<button class="button is-fullwidth is-loading is-link is-medium" />
	{:then}
		<table class="table is-fullwidth is-hoverable is-striped">
			<tbody>
				{#each Object.keys(topicDict) as topic}
					<tr
						on:click={() => {
							toggleTopic(topic);
						}}
						class="hover-cursor {selectedTopics.includes(topic)
							? 'is-selected'
							: ''}"
					>
						<td>
							<input
								type="checkbox"
								class="checkbox"
								bind:group={selectedTopics}
								value={topic}
							/>
							{topic}
						</td>
						<td class="has-text-right">
							({topicDict[topic]})
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{/await}
</div>

<style>
	.hover-cursor {
		cursor: pointer;
	}
</style>
