<script lang="ts">
	import { goto } from "$app/navigation";
	import PageHeader from "$lib/PageHeader.svelte";
	import StdContainer from "$lib/StdContainer.svelte";
	import {
		QuestionState,
		type GameManager,
		type QuestionUI,
	} from "$lib/game";
	import { gameManagerStore } from "$lib/state";
	import Question from "./question/Question.svelte";

	let gameManager: GameManager | undefined;
	let currentQuestion: QuestionUI;
	let questionAnswerState: QuestionState = QuestionState.UNANSWERED;

	// --- Ensure the game is in a valid state
	gameManagerStore.subscribe((value) => {
		gameManager = value;
	});

	if (!gameManager) {
		goto("/");
	}

	// used by many things
	currentQuestion = gameManager!.getQuestion();

	// --- set UI components
	$: qIndex = "Question " + (currentQuestion.qIndex + 1);

	// --- handle answer selection
	function handleAnswersSelected(event: any) {
		if (gameManager!.answerQuestion(event.detail.answers)) {
			questionAnswerState = QuestionState.TRUE;
		} else {
			questionAnswerState = QuestionState.FALSE;
		}
	}
</script>

<PageHeader bind:text={qIndex} />

<StdContainer>
	<Question
		bind:question={currentQuestion.question}
		on:answersSelected={handleAnswersSelected}
	/>
	{#if questionAnswerState != QuestionState.UNANSWERED}
		{#if questionAnswerState == QuestionState.TRUE}
			true
		{:else}
			false
		{/if}
		next button
	{/if}
</StdContainer>
