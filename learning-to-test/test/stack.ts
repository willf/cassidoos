import { expect } from 'chai';
import { Stack } from '../src';
import { describe, it } from 'mocha';

describe('Stack', () => {
    it('false is false', () => {
      expect(false).to.be.false;
    });
  
    it('true is false', () => {
      const s = new Stack<number>();
      expect(true).to.be.false;
    });
    
   
});
