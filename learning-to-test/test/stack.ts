import { expect } from 'chai';
import { Stack } from '../src';
import { describe, it } from 'mocha';

describe('Stack', () => {
    it('can be initialized without an initializer', () => {
      const s = new Stack<number>();
      expect(false).to.be.false;
    });
  
    it('can be initialized without an initializer', () => {
      const s = new Stack<number>();
      expect(true).to.be.false;
    });
    
   
});
