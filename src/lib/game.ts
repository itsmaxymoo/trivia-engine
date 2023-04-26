export interface Question {
	text: string,
	correctAnswers: Array<String>,
	falseAnswers: Array<String>
}

export interface QuestionQueueEntry {
	question: Question,
	state: QuestionState
}

export interface QuestionUI {
	question: Question,
	qIndex: number
}

export enum QuestionState {
	UNANSWERED,
	TRUE,
	FALSE
}

export interface GameSettings {
	totalQuestions: number
}

export class GameManager {
	private _settings: GameSettings;
	private _questionIndex: number;

	private _questionQueue: Array<QuestionQueueEntry>;

	constructor(settings: GameSettings, categorizedQuestionBank: { [topic: string]: Array<Question> }) {
		this._settings = settings;
		this._questionIndex = 0;

		this._questionQueue = this.constructQuestionQueue(categorizedQuestionBank);
		console.log(this);
	}

	public get settings() { return this._settings; }
	public get questionArray() { return this._questionQueue; }

	public hasNextQuestion(): boolean {
		return this._questionIndex + 1 < this.settings.totalQuestions;
	}

	public getQuestion(): QuestionUI {
		return {
			question: this._questionQueue[this._questionIndex].question,
			qIndex: this._questionIndex
		};
	}

	public getNextQuestion(): QuestionUI {
		++this._questionIndex;
		return this.getQuestion();
	}

	public answerQuestion(selectedAnswers: Array<String>): boolean {
		let compA: boolean = selectedAnswers.every((object, index) => this.getQuestion().question.correctAnswers.includes(object));
		let compB: boolean = this.getQuestion().question.correctAnswers.every((object, index) => selectedAnswers.includes(object));

		let correct: boolean = compA && compB;

		this._questionQueue[this._questionIndex].state = (correct ? QuestionState.TRUE : QuestionState.FALSE);

		return correct;
	}

	private constructQuestionQueue(categorizedQuestionBank: { [topic: string]: Array<Question> }): Array<QuestionQueueEntry> {
		let keys = Object.keys(categorizedQuestionBank);
		let questions: Array<QuestionQueueEntry> = [];

		for (let pickedQuestions: number = 0; pickedQuestions < this.settings.totalQuestions; ++pickedQuestions) {
			let key: number = pickedQuestions % keys.length;

			let bank: Array<Question> = categorizedQuestionBank[keys[key]];
			let randQi = Math.floor(Math.random() * bank.length);

			questions.push({
				question: bank[randQi],
				state: QuestionState.UNANSWERED
			});

			bank.splice(randQi, 1);
		}

		return questions;
	}
}
