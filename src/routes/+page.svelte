<script lang="ts">
	import PageHeader from "../lib/PageHeader.svelte";
	import StdContainer from "../lib/StdContainer.svelte";
	import StartButton from "./StartButton.svelte";
	import TopicList from "./TopicList.svelte";

	let selectedTopics: Array<String> = [];
</script>

<PageHeader />

<StdContainer>
	<TopicList bind:selectedTopics />
	<StartButton bind:selectedTopics />
</StdContainer>
