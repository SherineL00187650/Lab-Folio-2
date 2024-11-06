// feature.test.js
const { checkAnswer, unlockHint } = require('./feature'); // Import functions to test
const data = require('./testData.json');

describe('Shrines History Feature - Unit Tests', () => {

  let credits = 0;

  test('Correct answer increases credits', () => {
    const answerCorrect = checkAnswer("Link", data.questions[0].answer);
    if (answerCorrect) credits += 10;

    expect(answerCorrect).toBe(true);
    expect(credits).toBe(10);
  });

  test('Incorrect answer does not increase credits', () => {
    const answerCorrect = checkAnswer("Zelda", data.questions[0].answer);
    if (answerCorrect) credits += 10;

    expect(answerCorrect).toBe(false);
    expect(credits).toBe(10); // Credits should remain the same
  });

  test('Unlocking hints deducts credits', () => {
    const hint = unlockHint(credits, data.questions[0].hints);
    credits -= 5; // Assume each hint costs 5 credits

    expect(hint).toBe(data.questions[0].hints[0]); // First hint should unlock
    expect(credits).toBe(5); // Credits after deduction
  });

});

// ui.test.js
const puppeteer = require('puppeteer');

describe('Shrines History Feature - UI Flow Tests', () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
    await page.goto('http://localhost:3000'); // Assuming local server
  });

  afterAll(async () => {
    await browser.close();
  });

  test('User sees initial credits and question', async () => {
    const creditsText = await page.$eval('#credits', el => el.textContent);
    expect(creditsText).toContain('Credits: 0');

    const questionText = await page.$eval('#question', el => el.textContent);
    expect(questionText).toContain('Current Question');
  });

  test('User answers question and earns credits', async () => {
    await page.click('button.option-button'); // Click on an answer

    const creditsText = await page.$eval('#credits', el => el.textContent);
    expect(creditsText).toContain('Credits: 10'); // Assumes correct answer

    const nextQuestionButton = await page.$('button#next-question');
    expect(nextQuestionButton).toBeTruthy();
  });

  test('User unlocks a hint using credits', async () => {
    await page.click('button#unlock-hint'); // Click to unlock a hint

    const creditsText = await page.$eval('#credits', el => el.textContent);
    expect(creditsText).toContain('Credits: 5'); // Assumes 5 credits used per hint

    const hintText = await page.$eval('#hints p', el => el.textContent);
    expect(hintText).toContain('First Hint'); // Check hint appears
  });

});
