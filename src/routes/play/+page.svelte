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
	let hasNextQuestion: boolean;

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
	$: {
		currentQuestion;
		hasNextQuestion = gameManager!.hasNextQuestion();
	};

	// --- handle answer selection
	function handleAnswersSelected(event: any) {
		if (gameManager!.answerQuestion(event.detail.answers)) {
			questionAnswerState = QuestionState.TRUE;
		} else {
			questionAnswerState = QuestionState.FALSE;
		}
	}

	// --- increment question function
	function nextQuestion() {
		if (gameManager!.hasNextQuestion()) {
			currentQuestion = gameManager!.getNextQuestion();
			questionAnswerState = QuestionState.UNANSWERED;
		}
	}
</script>

<PageHeader bind:text={qIndex} />

<StdContainer>
	<Question
		bind:question={currentQuestion.question}
		bind:questionAnswerState
		on:answersSelected={handleAnswersSelected}
	/>

	{#if questionAnswerState != QuestionState.UNANSWERED}
		<p class="has-text-centered">
			<button class="button is-link is-outline" on:click={nextQuestion}>
				{hasNextQuestion ? "Next question >" : "See results"}
			</button>
		</p>
	{/if}
</StdContainer>
