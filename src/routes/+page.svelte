<script lang="ts">
	import { questionPath } from "$lib/const";
	import { GameManager, type Question } from "$lib/game";
	import PageHeader from "$lib/PageHeader.svelte";
	import { gameManager } from "$lib/state";
	import StdContainer from "$lib/StdContainer.svelte";
	import StartButton from "./StartButton.svelte";
	import TopicList from "./TopicList.svelte";

	let selectedTopics: Array<String> = [];
	let isLoading: boolean = false;

	async function loadQuestionBanks() {
		if (isLoading) return;
		isLoading = true;
		let completedRequests: number = 0;
		let categorizedQuestionBank: { [topic: string]: Array<Question> } = {};

		selectedTopics.forEach((topic) => {
			let request = fetch(
				encodeURI(questionPath + "/" + topic + ".json")
			);
			request.then((res) =>
				res.json().then((qa) => {
					categorizedQuestionBank[topic.toString()] = [];

					qa.forEach((q: { [id: string]: any }) => {
						categorizedQuestionBank[topic.toString()].push({
							text: q["question"],
							answer: q["answer"],
							falseAnswers: q["false_answers"],
						});
					});

					++completedRequests;

					if (completedRequests >= selectedTopics.length) {
						gameManager.set(
							new GameManager(
								{ totalQuestions: 10 },
								categorizedQuestionBank
							)
						);
					}
				})
			);
		});
	}
</script>

<PageHeader />

<StdContainer>
	<TopicList bind:selectedTopics />
	<StartButton
		bind:selectedTopics
		bind:isLoading
		on:click={() => {
			loadQuestionBanks();
		}}
	/>
</StdContainer>
