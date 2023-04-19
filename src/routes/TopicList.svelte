<script lang="ts">
	import { questionPath } from "$lib/const";

	let topicList: Array<String> = [];
	export let selectedTopics: Array<String> = [];

	async function loadTopicsList() {
		const res = await fetch(questionPath + "/_topics.json");
		const resp = await res.text();

		if (res.ok) {
			topicList = JSON.parse(resp);
			return true;
		} else {
			throw new Error(resp);
		}
	}

	let topicsPromise = loadTopicsList();
</script>

<div class="box">
	<h2 class="is-size-3 is-underlined">Topics</h2>

	{#await topicsPromise}
		<button class="button is-fullwidth is-loading is-link is-medium" />
	{:then}
		<table class="table is-fullwidth is-striped">
			<tbody>
				{#each topicList as topic}
					<tr class="{(selectedTopics.includes(topic)) ? "is-selected" : ""}">
						<td>
							<input type="checkbox" class="checkbox" bind:group={selectedTopics} value="{topic}"/>
							{topic}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{/await}
</div>
